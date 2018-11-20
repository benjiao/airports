from django.contrib.gis.db import models


class Airport(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    iata = models.CharField(max_length=3)
    icao = models.CharField(max_length=4)

    location = models.PointField(
        null=True,
        blank=True,
        spatial_index=True,
        dim=3)

    def __str__(self):
        return self.name
