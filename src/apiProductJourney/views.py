# from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    # Productjourney,
    Organization,
    Batchdetail,
    Facility,
    Certification,
    Transactionid,
    Walletaddress
)
from .serializers import (
    # ProductjourneySerializer,
    OrganizationSerializer,
    BatchdetailSerializer,
    FacilitySerializer,
    CertificationSerializer,
    TransactionidSerializer,
    WalletaddressSerializer
)


class TransactionidView(viewsets.ModelViewSet):
    queryset = Transactionid.objects.all()
    serializer_class = TransactionidSerializer


class WalletaddressView(viewsets.ModelViewSet):
    queryset = Walletaddress.objects.all()
    serializer_class = WalletaddressSerializer


# class ProductjourneyView(viewsets.ModelViewSet):
#    queryset = Productjourney.objects.all()
#    serializer_class = ProductjourneySerializer


class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BatchdetailView(viewsets.ModelViewSet):
    queryset = Batchdetail.objects.all()
    serializer_class = BatchdetailSerializer


class FacilityView(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class CertificationView(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
