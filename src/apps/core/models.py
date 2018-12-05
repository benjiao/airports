from django.contrib.gis.db import models


class Airport(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    iata = models.CharField(max_length=3, null=True)
    icao = models.CharField(max_length=4, null=True)

    location = models.PointField(
        null=True,
        blank=True,
        spatial_index=True,
        dim=3)

    evcent = models.FloatField(null=True)
    pagerank = models.FloatField(null=True)
    degree = models.FloatField(null=True)
    betweenness = models.FloatField(null=True)
    closeness = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    iata = models.CharField(max_length=3, null=True)
    icao = models.CharField(max_length=4, null=True)
    callsign = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    active = models.BooleanField()
    openflights_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    iata = models.CharField(max_length=3, null=True)
    icao = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    airline = models.ForeignKey(
        'core.Airline',
        on_delete=models.CASCADE,
        related_name='routes',
        null=True)

    equipment = models.ForeignKey(
        'core.Equipment',
        on_delete=models.CASCADE,
        related_name='routes',
        null=True)

    source = models.ForeignKey(
        'core.Airport',
        on_delete=models.CASCADE,
        related_name="routes_as_source",
        null=True)

    dest = models.ForeignKey(
        'core.Airport',
        on_delete=models.CASCADE,
        related_name="routes_as_dest",
        null=True)

    stops = models.IntegerField()
    codeshare = models.BooleanField()

    def __str__(self):
        return "{} to {}".format(self.source, self.dest)
