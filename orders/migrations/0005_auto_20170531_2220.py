# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170531_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena zamówienia bez dostawy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena z dostawą'),
        ),
    ]
