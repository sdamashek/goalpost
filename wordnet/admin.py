from django.contrib import admin
from models import Definition, Domain
import reversion

class DefinitionAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Domain)
