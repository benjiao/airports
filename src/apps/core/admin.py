from django.contrib.gis import admin
from . import models


class AirlineAdmin(admin.GeoModelAdmin):
    list_display = ['icao', 'iata', 'name', 'alias', 'country', 'openflights_id']


class AirportAdmin(admin.GeoModelAdmin):
    list_display = ['icao', 'iata', 'name', 'city', 'country', 'evcent', 'pagerank', 'degree']


class EquipmentAdmin(admin.GeoModelAdmin):
    list_display = ['icao', 'iata', 'name']


class RouteAdmin(admin.GeoModelAdmin):
    list_display = ['airline', 'source', 'dest', 'equipment', 'stops', 'codeshare']


admin.site.register(models.Airport, AirportAdmin)
admin.site.register(models.Airline, AirlineAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Route, RouteAdmin)
