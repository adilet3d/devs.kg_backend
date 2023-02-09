from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from apps.company.models import Company
from apps.vacancii.models import Vacancii
from apps.vacancii.serializers import VacanciiSerializer

class VacanciiView(ModelViewSet):
    queryset= Vacancii.objects.all()
    serializer_class=VacanciiSerializer