from django.conf.urls import *
from models import Definition
from views import DefinitionListView, DomainListView, definitionListByDomain, edit
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

urlpatterns = patterns('',
        url(r'^$', DefinitionListView.as_view()),
        url(r'^new/$', CreateView.as_view(model=Definition, fields=['term','definition'])),
        url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Definition)),
        url(r'^domain/$', DomainListView.as_view()),
        url(r'^domain/(?P<pk>\d+)/$', definitionListByDomain),
        url(r'^edit/$', edit),
       ) 
