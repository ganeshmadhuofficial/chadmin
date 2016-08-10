from __future__ import unicode_literals

from django.db import models

class Market(models.Model):
    class Meta:
        db_table = '"markets"'
    name          = models.CharField(max_length=255,null=False)
    code          = models.CharField(max_length=255,null=False)
    currency_code = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class Locale(models.Model):
    class Meta:
        db_table = '"locales"'
    name     = models.CharField(max_length=255,null=False)
    code     = models.CharField(max_length=255,null=False)
    mit_code = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class SourceType(models.Model):
    class Meta:
        db_table = '"source_types"'
    name       = models.CharField(max_length=255,null=False)
    reid_min   = models.IntegerField(null=False)
    reid_max   = models.IntegerField(null=False)
    group_name = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class Survey(models.Model):
    class Meta:
        db_table = '"surveys"'
    name       = models.CharField(max_length=255,null=False)
    url        = models.CharField(max_length=255,null=False)
    market     = models.ForeignKey(Market)
    locale     = models.ForeignKey(Locale)
    is_global  = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    begin_at   = models.CharField(max_length=200,null=True)
    end_at     = models.CharField(max_length=200,null=True)

class Distribution(models.Model):
    class Meta:
        db_table = '"distributions"'
    name           = models.CharField(max_length=255,null=False)
    survey         = models.ForeignKey(Survey)
    source_type    = models.ForeignKey(SourceType)
    reid           = models.IntegerField(null=False)
    is_default     = models.BooleanField(default=False)
    skip_opt_in    = models.BooleanField(default=False)
    skip_reid      = models.BooleanField(default=False)
