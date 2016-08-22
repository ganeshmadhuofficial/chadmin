from django.conf.urls import url
from .models import *
from distributions import views

urlpatterns = [
  url(r'^$', views.DistributionsView.as_view(), name='distributions'),
  url(r'^(?P<pk>[0-9]+)/$', views.DistributionView, name='distribution_detail'),
  url(r'^new/$',views.DistributionCreate, name='distribution_create'),
  url(r'^(?P<pk>[0-9]+)/edit/', views.DistributionUpdate, name='distribution_update'),
  url(r'^(?P<pk>[0-9]+)/delete/', views.DistributionDelete, name='distribution_delete')
]
