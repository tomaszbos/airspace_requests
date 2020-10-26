from django.contrib.gis.utils import LayerMapping

from .models import WorldBorder


world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}


def run(verbose=True):
    """
    Function for putting data into DB.
    """
    lm = LayerMapping(WorldBorder,
                      '/home/tb/DEV/airspace_request/structures_api/data/TM_WORLD_BORDERS-0.3.shp',
                      world_mapping,
                      transform=False
                      )
    lm.save(strict=True, verbose=verbose)
