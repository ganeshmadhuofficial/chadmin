from django import forms
from surveys import models

class DistributionForm(forms.ModelForm):
  class Meta:
    model  = models.Distribution
    fields = ['name','survey','source_type','reid','skip_reid','skip_opt_in','is_default']
