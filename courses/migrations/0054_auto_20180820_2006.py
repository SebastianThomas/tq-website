# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0053_voucher_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='voucher/'),
        ),
    ]