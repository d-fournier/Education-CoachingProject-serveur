# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20160216_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='isPinned',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
