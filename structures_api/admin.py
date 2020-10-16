from django.contrib import admin

from .models import AirspaceStructure


@admin.register(AirspaceStructure)
class AirspaceStructuresAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name', 'airspace_type']
    list_display = ('name', 'airspace_type', 'lower_limit', 'upper_limit')
    admin.site.site_header = 'Airspace application administration'
    admin.site.index_title = 'Authentication, Authorization and Airspace Structures administration'
