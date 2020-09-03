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

    class Meta:
        model = Transactionid
        fields = ('uuid', 'txid')


class WalletaddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walletaddress
        fields = ('uuid', 'name')


class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification
        fields = ('uuid', 'name', 'txid', 'wallet')


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ('uuid', 'name', 'txid', 'wallet')


class BatchdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batchdetail
        fields = ('uuid', 'name', 'wallet')


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('uuid', 'name', 'txid', 'wallet')


# class ProductjourneySerializer(serializers.ModelSerializer):
#
#    class Meta:
#        model = Productjourney
#        fields = ('uuid', 'organization', 'batchdetail',
#                  'facility', 'certification')
