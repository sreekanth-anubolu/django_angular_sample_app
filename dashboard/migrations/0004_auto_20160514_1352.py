# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20160514_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfoodsuggestions',
            name='apk_version',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
