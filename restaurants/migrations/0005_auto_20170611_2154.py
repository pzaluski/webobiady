# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20170611_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='category',
        ),
        migrations.RemoveField(
            model_name='dishcategory',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='DishCategory',
        ),
    ]
