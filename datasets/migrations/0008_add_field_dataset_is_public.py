# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-28 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0007_alter_meta_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Is public'),
        ),
    ]