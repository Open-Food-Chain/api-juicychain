from rest_framework import serializers
from .models import (
    # Productjourney,
    # Product,
    Organization,
    Batchdetail,
    Facility,
    Certificate,
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


class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    txid = TransactionidSerializer(read_only=True)
    wallet = WalletaddressSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'txid', 'wallet')


class CertificateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    txid = TransactionidSerializer(read_only=True)
    wallet = WalletaddressSerializer(read_only=True)

    class Meta:
        model = Certificate
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
