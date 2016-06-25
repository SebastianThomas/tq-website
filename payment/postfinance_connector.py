from django.conf import settings
from paramiko.client import SSHClient
import os

import logging
log = logging.getLogger('payment')


class FDSConnection():

    def __init__(self):
        self.client = SSHClient()
        self.client.load_host_keys(settings.FDS_HOST_KEY)
        self.client.connect(settings.FDS_HOST, username=settings.FDS_USER, key_filename=settings.FDS_PRIVATE_KEY, port=settings.FDS_PORT)
        self.sftp = self.client.open_sftp()
        log.info("Connected to FDS")

    def get_files(self):
        log.info("Receiving files from FDS...")
        fds_data_path = os.path.join(settings.BASE_DIR, settings.FDS_DATA_PATH)

        self.sftp.chdir('yellow-net-reports')
        for file in self.sftp.listdir('.'):
            log.info("Receiving {}".format(file))
            self.sftp.get(file, os.path.join(fds_data_path, file))
            #self.sftp.remove(file)

import xml.etree.ElementTree as ET
from payment.models import Payment
from datetime import datetime

class ISO2022Parser:

    def __init__(self):
        pass

    def parse(self):
        fds_data_path = os.path.join(settings.BASE_DIR, settings.FDS_DATA_PATH)
        log.debug("parse")
        for file in os.listdir(fds_data_path):
            if ('.xml' in file) and ('processed' not in file):
                filepath = os.path.join(fds_data_path, file)
                self.parse_file(filepath)

    def parse_file(self, filename):
        log.debug("parse file")

        tree = ET.parse(filename)
        root = tree.getroot()
        payments = []

        ns = {'pf': 'urn:iso:std:iso:20022:tech:xsd:camt.053.001.04'}

        def find_or_empty(transaction, name):
            e = transaction.find(".//pf:{}".format(name),ns)
            return e.text if e is not None else ""

        for transaction in root.findall(".//pf:Ntry",ns):
            log.debug("Processing Payment...")
            payment = Payment()
            #debitor = find_or_empty(transaction, "Dbtr")
            payment.bic = find_or_empty(transaction, 'BICFI')
            #payment.name = find_or_empty(debitor, 'Nm')
            payment.name = ""
            payment.iban = find_or_empty(transaction, 'DbtrAcct')
            payment.transaction_id = find_or_empty(transaction, 'AcctSvcrRef') # unique reference number by postfinance
            payment.amount = float(find_or_empty(transaction, 'Amt') or 0.0)
            payment.currency_code = transaction.find('.//pf:Amt', ns).get('Ccy')
            payment.remittance_user_string = find_or_empty(transaction, 'AddtlNtryInf')
            payment.state = Payment.State.NEW
            #postal_address = debitor.find(".//pf:PstlAdr",ns)
            #if postal_address:
            #    addresses = debitor.findall(".//pf:AdrLine", ns)
            #    payment.address = ", ".join([adr.text for adr in addresses])
            payment.date = datetime.today() # TODO not exactly elegant
            payment.filename = os.path.split(filename)[-1]
            payments.append(payment)
            log.info('Received payment by {}'.format(payment.name))

        for payment in payments:
            payment.save()

        os.rename(filename, filename + '.processed')