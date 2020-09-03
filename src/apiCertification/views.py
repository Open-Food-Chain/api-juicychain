# from django.shortcuts import render
from rest_framework import viewsets
from .models import Certificate, CertificateConditions
from .serializers import CertificateSerializer, CertificateConditionsSerializer


class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateConditionsView(viewsets.ModelViewSet):
    queryset = CertificateConditions.objects.all()
    serializer_class = CertificateConditionsSerializer
