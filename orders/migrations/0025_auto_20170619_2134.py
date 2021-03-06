# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20170616_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('NEW', 'Nowe'), ('ACCEPTED', 'Zamówione'), ('COMPLETED', 'Do odbioru'), ('REJECTED', 'Odrzucone')], default='NEW', max_length=10, verbose_name='Status zamówienia'),
        ),
    ]
