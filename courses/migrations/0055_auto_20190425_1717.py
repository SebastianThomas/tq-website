# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0054_auto_20180820_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voucher',
            options={'ordering': ['-issued', '-expires']},
        ),
    ]