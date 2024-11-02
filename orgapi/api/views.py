from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CompanySerializer
from api.models import Company
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer




