# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockdata',
            options={},
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='created',
        ),
    ]
