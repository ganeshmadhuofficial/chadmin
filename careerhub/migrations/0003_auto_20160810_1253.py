# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careerhub', '0002_auto_20160809_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribution',
            old_name='source_type_id',
            new_name='source_type',
        ),
        migrations.RenameField(
            model_name='distribution',
            old_name='survey_id',
            new_name='survey',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='locale_id',
            new_name='locale',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='market_id',
            new_name='market',
        ),
    ]
