# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20170625_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='mentor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmentor', to='oauth.UserProfile'),
        ),
    ]