from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from careerhub.forms import SurveyForm
from .models import Survey

# Create your views here.

def home(request):
  template = loader.get_template('careerhub/base.html')
  return render(request,'careerhub/base.html')

class SurveysView(generic.ListView):
  template_name = 'careerhub/surveys.html'
  context_object_name = 'latest_surveys'

  def get_queryset(self):
      return Survey.objects.all()

class SurveyCreate(generic.edit.CreateView):
  model  = Survey
  fields = ['name','url']

def SurveyView(request,pk):
  model = Survey
  template_name = 'careerhub/survey_form.html'
  my_record = Survey.objects.get(id=pk)
  form = SurveyForm(instance=my_record)
  context = {
    "form": form,
    "instance": my_record
  }
  success_url = '/surveys/'
  return render(request,template_name,context)

def SurveyUpdate(request,pk):
  my_record = Survey.objects.get(id=pk)
  form = SurveyForm(request.POST or None)
  template_name = 'careerhub/survey_form.html'
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
  context = {
    "form": form,
    "instance": my_record
  }
  return render(request,template_name,context)

def surveys(request):
  context = dict()
  context['surveys'] = Survey.objects.all()
  return render(request,'careerhub/surveys.html',context)

