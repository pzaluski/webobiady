# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_order_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Zamówienie', 'verbose_name_plural': 'Zamówienie'},
        ),
        migrations.AlterModelOptions(
            name='ordersettings',
            options={'verbose_name': 'Ustawienia zamówień', 'verbose_name_plural': 'Ustawienia zamówień'},
        ),
        migrations.RemoveField(
            model_name='ordersettings',
            name='order_date',
        ),
        migrations.AlterField(
            model_name='ordersettings',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant', verbose_name='Restauracja'),
        ),
    ]