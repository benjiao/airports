from rest_framework import serializers
from apps.core.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    sources = serializers.SerializerMethodField()
    destinations = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Airport

    def get_destinations(self, obj):
        return [x.dest.id if x.dest is not None else None for x in obj.routes_as_source.all()]

    def get_sources(self, obj):
        return [x.source.id if x.source is not None else None for x in obj.routes_as_dest.all()]

    def get_location(self, obj):
        if obj.location:
            return obj.location.coords[:2]
        else:
            return None
