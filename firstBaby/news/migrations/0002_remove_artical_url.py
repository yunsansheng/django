# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical',
            name='url',
        ),
    ]
