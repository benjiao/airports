from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.core.models import Airport
from apps.core.models import Route
from django.db.models import Count

from apps.core.serializers import AirportSerializer


@api_view()
def get_airports(request):
    airports = Airport.objects \
        .annotate(source_count=Count('routes_as_source')) \
        .annotate(dest_count=Count('routes_as_dest')) \
        .filter(source_count__gt=0, dest_count__gt=0) \
        .all()

    return Response({
        "data": AirportSerializer(airports, many=True).data
    })
