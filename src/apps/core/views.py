from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.core.models import Airport
from apps.core.models import Route

from apps.core.serializers import AirportSerializer


@api_view()
def get_airports(request):
    airports = Airport.objects.all()

    return Response({
        "data": AirportSerializer(airports, many=True).data
    })
