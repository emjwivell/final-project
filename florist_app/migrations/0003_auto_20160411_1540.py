# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('florist_app', '0002_arrangement_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arrangement',
            options={'ordering': ['-time_created']},
        ),
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ['-time_created']},
        ),
        migrations.RemoveField(
            model_name='florist',
            name='arrangement_history',
        ),
        migrations.AddField(
            model_name='arrangement',
            name='florist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='florist_app.Florist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrangement',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 11, 15, 40, 58, 457029, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
