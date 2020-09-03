from rest_framework import serializers
from .models import BatchesRefresco


class BatchesRefrescoSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = BatchesRefresco
        fields = ('uuid', 'anfp', 'dfp', 'bnfp', 'pds', 'pde', 'jds', 'jde', 'bbd', 'pc', 'pl', 'rmn', 'pon', 'pop')
