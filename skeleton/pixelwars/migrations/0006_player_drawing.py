# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelwars', '0005_auto_20170323_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='drawing',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
