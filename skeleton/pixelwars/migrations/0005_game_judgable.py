# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelwars', '0004_auto_20170325_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='judgable',
            field=models.BooleanField(default=False),
        ),
    ]