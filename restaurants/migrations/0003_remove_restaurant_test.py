# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='test',
        ),
    ]
