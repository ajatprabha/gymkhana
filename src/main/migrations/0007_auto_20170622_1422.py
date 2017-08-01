# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 08:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170622_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='society',
            options={'ordering': ['name'], 'verbose_name_plural': 'Societies'},
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]