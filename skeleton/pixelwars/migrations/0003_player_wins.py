# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelwars', '0002_auto_20170320_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.IntegerField(null=1),
        ),
    ]
