# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
    ]
