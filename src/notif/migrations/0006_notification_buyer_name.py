# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-07 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notif', '0005_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='buyer_name',
            field=models.CharField(blank=True, help_text='Full name.', max_length=30),
        ),
    ]