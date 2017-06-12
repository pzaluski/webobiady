# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20170612_2144'),
        ('orders', '0016_auto_20170612_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(default=None, null=True, to='restaurants.Dish'),
        ),
    ]
