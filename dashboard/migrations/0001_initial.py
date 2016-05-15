# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFoodSuggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.BigIntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('apk_version', models.IntegerField(blank=True, null=True)),
                ('subscription_type', models.IntegerField(null=True)),
                ('suggested_food', models.CharField(max_length=200)),
                ('problem', models.IntegerField(default=0)),
                ('same_as', models.CharField(max_length=50)),
                ('action_taken', models.BooleanField(default=False)),
                ('gcm_push', models.BooleanField(default=False)),
                ('email_status', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
