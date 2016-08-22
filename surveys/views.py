from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from surveys.forms import SurveyForm
from .models import Survey

# Create your views here.

def home(request):
  template = loader.get_template('surveys/base.html')
  return render(request,'surveys/base.html')

class SurveysView(generic.ListView):
  template_name = 'surveys/surveys.html'
  context_object_name = 'latest_surveys'

  def get_queryset(self):
      return Survey.objects.all()

def SurveyCreate(request):
  form = SurveyForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return redirect("surveys:surveys")
  context = {
    "form": form,
  }
  return render(request, "surveys/new.html", context)

def SurveyView(request,pk):
  template_name = 'surveys/show.html'
  context = {
    "instance": Survey.objects.get(id=pk)
  }
  return render(request,template_name,context)

def SurveyUpdate(request,pk):
  instance = Survey.objects.get(id=pk)
  form = SurveyForm(request.POST or None, instance=instance)
  template_name = 'surveys/edit.html'
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return redirect('surveys:surveys')
  context = {
    "form": form,
    "instance": instance
  }
  return render(request,template_name,context)

def SurveyDelete(request,pk):
  instance = get_object_or_404(Survey, id=pk)
  instance.delete()
  return redirect("surveys:surveys")

def surveys(request):
  context = dict()
  context['surveys'] = Survey.objects.all()
  return render(request,'surveys/surveys.html',context)

