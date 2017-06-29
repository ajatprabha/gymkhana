# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 18:50
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_update_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Upload high quality image to use as cover photo.', null=True, upload_to='news_%Y'),
        ),
    ]
