# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='files/%Y/%m/%d'),
        ),
    ]
