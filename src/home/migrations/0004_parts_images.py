# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-22 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180507_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='images',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]