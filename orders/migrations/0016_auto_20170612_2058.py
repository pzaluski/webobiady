# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 18:58
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Dish'),
        ),
    ]
