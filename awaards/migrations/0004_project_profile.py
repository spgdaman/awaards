# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awaards', '0003_auto_20190525_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='awaards.Profile'),
            preserve_default=False,
        ),
    ]