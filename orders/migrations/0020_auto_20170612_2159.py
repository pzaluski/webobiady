# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20170612_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cena z dostawą'),
        ),
    ]
