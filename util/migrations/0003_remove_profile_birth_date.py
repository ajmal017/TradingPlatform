# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0002_auto_20170608_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
