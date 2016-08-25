from django import forms
from surveys import models
from django.core.exceptions import ValidationError
import re

class SurveyForm(forms.ModelForm):
  class Meta:
    model  = models.Survey
    fields = ['id','name','url','is_global','is_special','begin_at','end_at','market','locale']

  def clean_name(self):
    value = self.cleaned_data.get('name')
    reg = re.compile('^[^\s]+$')
    if reg.search(value) is None:
        raise ValidationError('name cannot contain spaces')
    reg = re.compile('^[0-9a-zA-Z_]+$')
    if reg.search(value) is None:
        raise ValidationError('name can have alphanumeric and underscore')
    return self.cleaned_data.get('name')

  def clean_url(self):
    value = self.cleaned_data.get('url')
    reg = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if reg.search(value) is None:
        raise ValidationError('url is invalid')
    return self.cleaned_data.get('url')

  def clean(self):
    cleaned_data = super(SurveyForm, self).clean()
    globals = models.Survey.objects.filter(is_global=True)
    if cleaned_data.get('is_global') and globals:
        if globals.first().name != cleaned_data.get('name'):
            raise ValidationError('Only one global')
    return cleaned_data
