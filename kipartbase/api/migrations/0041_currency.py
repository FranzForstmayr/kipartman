# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20171005_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('symbol', models.TextField(default='')),
                ('base', models.TextField(default='EUR')),
                ('ratio', models.IntegerField()),
            ],
        ),
    ]
