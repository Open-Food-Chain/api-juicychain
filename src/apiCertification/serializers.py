from rest_framework import serializers
from .models import Certificate, CertificateConditions


class CertificateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'name')


class CertificateConditionsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = CertificateConditions
        fields = ('id', 'certificate_uuid')
