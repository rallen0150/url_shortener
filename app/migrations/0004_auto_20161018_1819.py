# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bookmark_new_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='bookmark',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
