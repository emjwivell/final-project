# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 16:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('florist_app', '0010_auto_20160417_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='order_history',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='florist',
            name='user',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='consumer',
            new_name='buyer',
        ),
        migrations.RemoveField(
            model_name='arrangement',
            name='florist',
        ),
        migrations.AddField(
            model_name='arrangement',
            name='posting_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Florist',
        ),
        migrations.AddField(
            model_name='user',
            name='order_history',
            field=models.ManyToManyField(to='florist_app.Cart'),
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
