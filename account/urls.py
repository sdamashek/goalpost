from django.conf.urls import *
import views

urlpatterns = patterns('',
        url(r'^login/$', views.login),
        url(r'^create/$', views.create_account),
       ) 
