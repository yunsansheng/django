# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170615_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='question_no',
            field=models.IntegerField(default=0),
        ),
    ]
