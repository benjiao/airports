from django.urls import path
from apps.core.views import get_airports

urlpatterns = [
    path('api/airports/', get_airports),
]
