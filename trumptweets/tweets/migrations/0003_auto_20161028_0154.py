# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20161020_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
