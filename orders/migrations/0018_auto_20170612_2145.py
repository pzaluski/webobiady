# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20170612_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(default=None, to='restaurants.Dish'),
        ),
    ]