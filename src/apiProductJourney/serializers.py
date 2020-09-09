from rest_framework import serializers
from .models import (
    # Productjourney,
    # Product,
    Organization,
    Batchdetail,
    Facility,
    Certification,
    Walletaddress,
    Transactionid
)


class TransactionidSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Transactionid
        fields = ('id', 'txid')


class WalletaddressSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Walletaddress
        fields = ('id', 'name')


class CertificationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Certification
        fields = ('id', 'name', 'txid', 'wallet')


class FacilitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Facility
        fields = ('id', 'name', 'txid', 'wallet')


class BatchdetailSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Batchdetail
        fields = ('id', 'name', 'wallet')


class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'txid', 'wallet')
