# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_modification_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 10, 18, 13, 58, 801019, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
