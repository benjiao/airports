from django.contrib.gis import admin
from . import models


class AirportAdmin(admin.GeoModelAdmin):
    list_display = ['icao', 'iata', 'name', 'city', 'country']


admin.site.register(models.Airport, AirportAdmin)
