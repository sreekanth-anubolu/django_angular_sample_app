# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfoodsuggestions',
            name='action_taken',
            field=models.CharField(max_length=200),
        ),
    ]
