from rest_framework import serializers
from .models import Certificate, CertificateConditions


class CertificateSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Certificate
        fields = ('uuid', 'name')


class CertificateConditionsSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = CertificateConditions
        fields = ('uuid', 'certificate_uuid')
