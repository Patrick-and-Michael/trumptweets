# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='author_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.BigIntegerField(),
        ),
    ]