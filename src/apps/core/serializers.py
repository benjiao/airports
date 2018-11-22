from rest_framework import serializers
from apps.core.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    destinations = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Airport

    def get_destinations(self, obj):
        return [x.dest.id if x.dest is not None else None for x in obj.routes_as_source.all()]
