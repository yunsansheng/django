# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sourcefrom', models.CharField(max_length=60)),
                ('source_topic', models.CharField(max_length=60)),
                ('topic_no', models.IntegerField(default=0)),
                ('url', models.TextField(null=True)),
                ('vote', models.CharField(max_length=30)),
                ('lable', models.TextField(null=True)),
            ],
        ),
    ]
