# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixelwars', '0010_auto_20170326_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='drawing1',
            field=models.ImageField(default=None, upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='drawing2',
            field=models.ImageField(default=None, upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='drawing3',
            field=models.ImageField(default=None, upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='drawing4',
            field=models.ImageField(default=None, upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='player1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tourneyplayer1', to='pixelwars.Player'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='player2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tourneyplayer2', to='pixelwars.Player'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='player3',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tourneyplayer3', to='pixelwars.Player'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='player4',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tourneyplayer4', to='pixelwars.Player'),
        ),
    ]
