# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-13 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20170810_1104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PartStorages',
            new_name='PartStorage',
        ),
    ]