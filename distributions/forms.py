from django import forms
from surveys import models
from django.core.exceptions import ValidationError
import re

class DistributionForm(forms.ModelForm):
  class Meta:
    model  = models.Distribution
    fields = ['name','survey','source_type','skip_reid','skip_opt_in','is_default']

  def clean_name(self):
    value = self.cleaned_data.get('name')
    space = re.compile('^[^\s]+$')
    alnum = re.compile('^[0-9a-z]+$')
    value = re.sub("\s\s+", " ", value).strip()
    if space.search(value) is None or alnum.search(value) is None:
        raise ValidationError('name can have alphanumeric characters without spaces and special characters')
    return value

  def clean(self):
    cleaned_data  = super(DistributionForm, self).clean()
    default_dists = models.Distribution.objects.filter(is_default=True,survey=cleaned_data.get('survey')).exclude(name=cleaned_data.get('name'))
    if cleaned_data.get('is_default') and default_dists:
        raise ValidationError('Only one default distribution for a survey')
    return cleaned_data
