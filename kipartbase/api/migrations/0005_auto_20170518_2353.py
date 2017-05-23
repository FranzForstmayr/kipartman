# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_part_mataparts'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetapartPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='part',
            name='mataparts',
        ),
        migrations.AddField(
            model_name='metapartpart',
            name='part',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Part'),
        ),
    ]
