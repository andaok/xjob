# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ng_name', models.CharField(max_length=50, unique=True)),
                ('vip', models.CharField(max_length=50, unique=True)),
                ('nodes_ip', models.CharField(max_length=128)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
