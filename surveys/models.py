from __future__ import unicode_literals

from django.utils import timezone
from django.db.models.signals import pre_save
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

import re

class Market(models.Model):
    class Meta:
        db_table = "markets"
    name          = models.CharField(max_length=255,null=False)
    code          = models.CharField(max_length=255,null=False)
    currency_code = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class Locale(models.Model):
    class Meta:
        db_table = "locales"
    name     = models.CharField(max_length=255,null=False)
    code     = models.CharField(max_length=255,null=False)
    mit_code = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class SourceType(models.Model):
    class Meta:
        db_table =  "source_types"
    name       = models.CharField(max_length=255,null=False)
    reid_min   = models.IntegerField(null=False)
    reid_max   = models.IntegerField(null=False)
    group_name = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name

class Survey(models.Model):
    Statuses = (
        ('online','online'),
        ('paused','paused'),
        ('offline','offline')
    )
    class Meta:
        db_table = "surveys"
    name       = models.CharField(max_length=255,null=False,unique=True)
    url        = models.CharField(max_length=255,null=False)
    market     = models.ForeignKey(Market)
    locale     = models.ForeignKey(Locale)
    is_global  = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    begin_at   = models.CharField(max_length=200,blank=True)
    end_at     = models.CharField(max_length=200,blank=True)
    status     = models.CharField(max_length=50,choices=Statuses,default='offline')
    created    = models.DateTimeField(default=timezone.now,null=True)
    updated    = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
    	return self.name

class Distribution(models.Model):
    class Meta:
        db_table = "distributions"
    name           = models.CharField(max_length=255,null=False,unique=True)
    survey         = models.ForeignKey(Survey)
    source_type    = models.ForeignKey(SourceType)
    reid           = models.IntegerField(null=False)
    is_default     = models.BooleanField(default=False)
    skip_opt_in    = models.BooleanField(default=False)
    skip_reid      = models.BooleanField(default=False)
    created        = models.DateTimeField(default=timezone.now,null=True)
    updated        = models.DateTimeField(auto_now=True,null=True)

    def __str_(self):
	return self.name

def pre_save_survey(sender,instance,*args,**kwargs):
    instance.name = re.sub("\s\s+", " ", instance.name).strip()
    instance.url  = re.sub("\s\s+", " ", instance.url).strip()


pre_save.connect(pre_save_survey, sender=Survey)
