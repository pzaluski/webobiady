# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_category_dish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='category',
            new_name='categories',
        ),
    ]
