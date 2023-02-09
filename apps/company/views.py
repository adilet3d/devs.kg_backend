from django.shortcuts import render
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from apps.company.models import Company
from apps.company.serializers import CompanySerializer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response



class CompanyView(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )

    # @action(methods=['post'],detail=True, permission_classes=\
    #     (permissions.IsAuthenticated,))
        
    # def add_company(self ,request, *args,**kwargs):
    #     serializer=CompanySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data= serializer.validated_data
    #     company=Company.objects.create(
    #         name=data.get('name'),
    #         description=data.get('description'),
    #         logo=data.get('logo'),
    #         telegram=data.get('telegram'),
    #         whatsapp=data.get('whatsapp'),
    #     )
    #     return Response(CompanySerializer(company).data)

