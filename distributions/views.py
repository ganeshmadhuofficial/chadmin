from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from django.views import generic
from .forms import DistributionForm
from surveys.models import Distribution

class DistributionsView(generic.ListView):
  template_name = 'distributions/distributions.html'
  context_object_name = 'latest_distributions'

  def get_queryset(self):
      return Distribution.objects.all()

def DistributionCreate(request):
  form = DistributionForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Successfully Created")
    return redirect("distributions:distributions")
  context = {
    "form": form,
  }
  return render(request, "distributions/new.html", context)

def DistributionView(request,pk):
  template_name = 'distributions/show.html'
  context = {
    "instance": Distribution.objects.get(id=pk)
  }
  return render(request,template_name,context)

def DistributionUpdate(request,pk):
  instance = Distribution.objects.get(id=pk)
  form = DistributionForm(request.POST or None, instance=instance)
  template_name = 'distributions/edit.html'
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Successfully Updated")
    return redirect('distributions:distributions')
  context = {
    "form": form,
    "instance": instance
  }
  return render(request,template_name,context)

def DistributionDelete(request,pk):
  instance = get_object_or_404(Distribution, id=pk)
  instance.delete()
  messages.success(request, "Successfully Deleted")
  return redirect("distributions:distributions")

