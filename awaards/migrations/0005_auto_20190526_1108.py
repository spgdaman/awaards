# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaards', '0004_project_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='design_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='usability_rating',
            field=models.IntegerField(default=0),
        ),
    ]
