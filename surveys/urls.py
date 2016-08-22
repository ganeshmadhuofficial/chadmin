from django.conf.urls import url
from .models import *
from surveys import views

urlpatterns = [
  url(r'^$', views.SurveysView.as_view(), name='surveys'),
  url(r'^(?P<pk>[0-9]+)/$', views.SurveyView, name='survey_detail'),
  url(r'^new/$',views.SurveyCreate, name='survey_create'),
  url(r'^(?P<pk>[0-9]+)/edit/', views.SurveyUpdate, name='survey_update'),
  url(r'^(?P<pk>[0-9]+)/delete/', views.SurveyDelete, name='survey_delete')
]
