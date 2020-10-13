from django.contrib import admin

from .models import AirspaceStructure


@admin.register(AirspaceStructure)
class AirspaceStructuresAdmin(admin.ModelAdmin):
    list_display = ('name', 'airspace_type')
    site_header = 'Airspace requests and structures administration'
