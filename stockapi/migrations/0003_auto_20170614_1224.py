# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapi', '0002_auto_20170612_1736'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pointers',
            unique_together=set([('ticker', 'interval')]),
        ),
    ]
