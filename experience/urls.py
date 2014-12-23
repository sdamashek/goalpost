from django.conf.urls import *
from models import Experience, Resource, Involvement
from views import *
from djangoratings.views import AddRatingFromModel

urlpatterns = patterns('',
#    url(r'^resource/new/$', ResourceCreateView.as_view()),
#    url(r'^resource/$', ResourceListView.as_view()),
    url(r'^camp/new/$', CampCreateView.as_view()),
    url(r'^camp/$', CampListView.as_view()),
    url(r'^camps/$', list_camp_urls),
    url(r'^rate-camp/(?P<object_id>\d+)/(?P<score>\d+)/$', AddRatingFromModel(), {
        'app_label': 'experience',
        'model': 'camp',
        'field_name': 'rating',
        }),
    url(r'', ExperienceListView.as_view()),
    )