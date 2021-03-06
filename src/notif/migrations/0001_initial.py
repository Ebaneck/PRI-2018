# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-01 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('buyer_id', models.PositiveIntegerField()),
                ('part_id', models.BooleanField()),
                ('message', models.CharField(help_text='Message for user about notification', max_length=255)),
            ],
            options={
                'verbose_name': 'Parts',
                'verbose_name_plural': 'Parts',
            },
        ),
    ]
