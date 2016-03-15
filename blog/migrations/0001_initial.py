# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 17:25
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sport', '0001_initial'),
        ('user', '0007_userprofile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('content', models.TextField()),
                ('picture', models.ImageField(blank=True, default=None, null=True, upload_to=blog.models.blog_directory_path)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserProfile')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.Sport')),
            ],
        ),
    ]