from django import forms
from surveys import models
from django.core.exceptions import ValidationError
import re

class SurveyForm(forms.ModelForm):
  class Meta:
    model  = models.Survey
    fields = ['id','name','url','market','locale','status','begin_at','end_at','is_global','is_special']

  def clean_name(self):
    value = self.cleaned_data.get('name')
    space = re.compile('^[^\s]+$')
    alnum = re.compile('^[0-9a-zA-Z_]+$')
    value = re.sub("\s\s+", " ", value).strip()
    if space.search(value) is None or alnum.search(value) is None:
        raise ValidationError('name can have alphanumeric and underscore and cannot contain spaces')
    return value

  def clean_url(self):
    value = self.cleaned_data.get('url')
    value = re.sub("\s\s+", " ", value).strip().lower()
    reg = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if reg.search(value) is None:
        raise ValidationError('url is invalid')
    return value

  def clean(self):
    cleaned_data = super(SurveyForm, self).clean()
    globals = models.Survey.objects.filter(is_global=True)
    if cleaned_data.get('is_global') and globals:
        if globals.first().name != cleaned_data.get('name'):
            raise ValidationError('Only one global')

    status = cleaned_data.get('status')
    if status == 'online' and cleaned_data.get('is_special') is False:
        live_surveys = models.Survey.objects.filter(market_id=cleaned_data.get('market'),status='online',is_special=False).exclude(name=cleaned_data.get('name'))
        if live_surveys:
            raise ValidationError('Only one non-special survey can be live for a market')

    return cleaned_data
