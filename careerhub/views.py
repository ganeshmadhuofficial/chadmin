from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SourceType

# Create your views here.

def home(request):
  template = loader.get_template('careerhub/base.html')
  return render(request,'careerhub/base.html')

def surveys(request):
  context = dict()
  context['surveys'] = SourceType.objects.all()
  return render(request,'careerhub/surveys.html',context)

