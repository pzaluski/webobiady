# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20170612_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategoria'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Danie', 'verbose_name_plural': 'Danie'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Restauracja', 'verbose_name_plural': 'Restauracja'},
        ),
    ]
