# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20170603_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersettings',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]