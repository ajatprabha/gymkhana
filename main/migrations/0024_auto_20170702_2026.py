# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20170702_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='senatemembership',
            name='year',
            field=models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], default=2, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='senatemembership',
            name='role',
            field=models.CharField(choices=[('SECY', 'Secretary'), ('SER', 'Student Elected Representative')], max_length=5),
        ),
    ]