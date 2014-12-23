from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
admin.autodiscover()

def index_view(request):
    return render(request, 'index.html')

urlpatterns = patterns('',
    url(r'^$', index_view),
# Wordnet
    url(r'^wordnet/', include('wordnet.urls')),
# Account
    url(r'^account/', include('account.urls')),
# Admin
    url(r'^admin/', include(admin.site.urls)),
# Experiences
    url(r'^experience/', include('experience.urls')),
    url(r'^stars/', include('rating.urls')),
)
