# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170814_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='source_url',
            field=models.URLField(null=True),
        ),
    ]
