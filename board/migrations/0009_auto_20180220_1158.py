# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20180220_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]