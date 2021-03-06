from django.contrib import admin
from django.contrib.gis import admin as geo_admin

from .models import AirspaceStructure, Aup, Reservation, WorldBorder


@admin.register(AirspaceStructure)
class AirspaceStructuresAdmin(geo_admin.OSMGeoAdmin):
    """
    Admin for Airspace structures.
    """
    ordering = ['name']
    search_fields = ['name', 'airspace_type']
    list_display = ('name', 'airspace_type', 'lower_limit', 'upper_limit')
    admin.site.site_header = 'Airspace application administration'
    admin.site.index_title = 'Authentication, Authorization and Airspace Structures administration'
    list_filter = ('airspace_type',)


@admin.register(Aup)
class AupAdmin(admin.ModelAdmin):
    """
    Admin for Aup.
    """
    ordering = ['creation_time']
    search_fields = ['validity_time_since', 'validity_time_to']
    list_display = ('creation_time', 'validity_time_since', 'validity_time_to')
    list_filter = ('validity_time_since',)


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    """
    Admin for reservations.
    """
    ordering = ['airspace_structure']
    list_display = ('airspace_structure',
                    'activation_date',
                    'deactivation_date',
                    'activation_time',
                    'deactivation_time',
                    'lower_limit',
                    'upper_limit',
                    )
    list_filter = ('airspace_structure', 'activation_date', 'activation_time', 'deactivation_time',)


admin.site.register(WorldBorder, geo_admin.OSMGeoAdmin)
