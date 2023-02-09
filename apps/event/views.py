from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from apps.company.models import Company
from apps.event.models import Event
from apps.event.serializers import EventSerializer



class EventView(ModelViewSet):
    queryset=Event.objects.all()
    serializer_class= EventSerializer