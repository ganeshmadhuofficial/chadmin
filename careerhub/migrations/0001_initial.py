# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reid', models.IntegerField()),
                ('is_default', models.BooleanField(default=False)),
                ('skip_opt_in', models.BooleanField(default=False)),
                ('skip_reid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('mit_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('currency_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reid_min', models.IntegerField()),
                ('reid_max', models.IntegerField()),
                ('group_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('is_global', models.BooleanField(default=False)),
                ('is_special', models.BooleanField(default=False)),
                ('begin_at', models.CharField(max_length=200, null=True)),
                ('end_at', models.CharField(max_length=200, null=True)),
                ('locale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerhub.Locale')),
                ('market_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerhub.Market')),
            ],
        ),
        migrations.AddField(
            model_name='distribution',
            name='source_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerhub.SourceType'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='survey_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerhub.Survey'),
        ),
    ]
