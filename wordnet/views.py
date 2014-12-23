from django.shortcuts import render
from sortable_listview import SortableListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from models import Definition, Domain
from django.core.paginator import Paginator
from django.http import HttpResponse

import json

class DefinitionListView(SortableListView):
    allowed_sort_fields = {'term': {'default_direction': '',
                                    'verbose_name': 'Term'}}
    default_sort_field = 'term'
    paginate_by = 100
    template_name = 'definition_list.html'
    model = Definition

class DomainListView(SortableListView):
    allowed_sort_fields = {'name': {'default_direction': '',
                                    'verbose_name': 'Name'}}
    default_sort_field = 'name'
    paginate_by = 100
    template_name = 'domain_list.html'
    model = Domain

class DefinitionDetailView(DetailView):
	model = Definition

def definitionListByDomain(request, pk):
    definitions = Definition.objects.filter(domain__id = pk)
    p = Paginator(definitions, 10)
    page = p.page(int(request.GET.get('page','1')))
    return render(request, 'wordnet/definition_list.html', {'object_list':page.object_list})

def edit(request):
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponse("Invalid request", status=400)
    data = json.loads(request.body)
    entry = Definition.objects.get(id=data['id'])
    if not entry:
        return HttpResponse("No such object", status=400)
    setattr(entry, data['field'], data['value'])
    entry.save()
    return HttpResponse("OK")
