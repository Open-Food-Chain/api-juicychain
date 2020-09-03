# from django.shortcuts import render
from rest_framework import viewsets
from .models import BatchesRefresco
from .serializers import BatchesRefrescoSerializer


class BatchesRefrescoView(viewsets.ModelViewSet):
    queryset = BatchesRefresco.objects.all()
    serializer_class = BatchesRefrescoSerializer
