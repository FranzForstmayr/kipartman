# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-30 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20170819_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='octopart_uid',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
