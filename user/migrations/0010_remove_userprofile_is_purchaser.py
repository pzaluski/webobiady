# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20170608_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_purchaser',
        ),
    ]
