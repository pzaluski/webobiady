# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_auto_20170701_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='menu_url',
            field=models.CharField(max_length=400),
        ),
    ]
