# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 18:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_category_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
    ]
