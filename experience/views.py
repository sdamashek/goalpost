from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from sortable_listview import SortableListView
from django.http import HttpResponse
from haversine import haversine
from pygeocoder import Geocoder
gc = Geocoder(api_key='AIzaSyDfIZV0ELnkxT0jWEr1L_Mf0qBy-M9nqhY')

from models import *

class CampCreateView(CreateView):
    model=Camp
    fields=['name','type','description']

class CampListView(SortableListView):
    allowed_sort_fields = {'name': {'default_direction': '',
                                    'verbose_name': 'Name'}}
    default_sort_field = 'name'
    paginate_by = 10
    template_name = 'camp_list.html'
    model = Camp

class ExperienceCreateView(CreateView):
    model=Experience
    fields=['user','type']

class ExperienceListView(SortableListView):
    allowed_sort_fields = {'user': {'default_direction': '',
                                    'verbose_name': 'User'},
                            'type': {'default_direction': '',
                                    'verbose_name': 'Type'}}
    default_sort_field = 'type'
    paginate_by = 100
    template_name = 'experience_list.html'
    model = Experience

class InvolvementListView(SortableListView):
    allowed_sort_fields = {'role': {'default_direction': '',
                                    'verbose_name': 'Role'}}
    default_sort_field = 'role'
    paginate_by = 100
    template_name = 'involvement_list.html'
    model = Involvement

class InvolvementCreateView(CreateView):
    model = Involvement
    fields = ['experience','role','resource']

def list_camp_urls(request):
    address = request.GET.get('address','6315 Tisbury Dr, Burke, VA 22015')
    radius = float(request.GET.get('radius','999999999999'))
    camps = Camp.objects.all()
    results = []
    coords = gc.geocode(address)[0].coordinates
    for camp in camps:
        if haversine(coords, (camp.latitude, camp.longitude), miles=True) <= radius:
            results.append(camp)
    return HttpResponse('<html><body>'+'<br>'.join(['<a href=%s>%s</a>' % (c.url, c.url) for c in results])+'</body></html>')