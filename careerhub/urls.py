from django.conf.urls import url
from .models import *
from careerhub import views

urlpatterns = [
  url(r'^$', views.SurveysView.as_view(), name='surveys'),
  url(r'^(?P<pk>[0-9]+)/$', views.SurveyView, name='survey'),
  url(r'^(?P<pk>[0-9]+)/edit/', views.SurveyUpdate, name='survey_update'),
]
