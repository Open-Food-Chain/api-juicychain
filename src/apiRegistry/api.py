from rest_framework import routers, serializers, viewsets
from django.core.validators import RegexValidator
from .models import (
    Organization,
    Certificate,
    CertificateRule,
    Location,
    Batch,
    PoolPurchaseOrder,
    PoolBatch
)


# TODO remove
class BaseWalletSerializer0(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'blah']


class BaseWalletSerializer(serializers.ModelSerializer):
    # TODO when using uuid
    # id = serializers.UUIDField(read_only=True)
    pubkey = serializers.CharField(
        max_length=66,
        validators=[
            RegexValidator(
                regex='^.{66}$',
                message='Incorrect pubkey length, must be 66',
                code='pubkey66')])
    raddress = serializers.CharField(
        max_length=34,
        validators=[
            RegexValidator(
                regex='^.{34}$',
                message='Incorrect raddress length, must be 34',
                code='raddress34')])

    class Meta:
        # abstract = True
        fields = ['id', 'pubkey', 'raddress']


class OrganizationSerializer(BaseWalletSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'name', 'pubkey', 'raddress']


class CertificateRulesSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.UUIDField(read_only=True)

    class Meta:
        model = CertificateRule
        exclude = ['url']


class CertificateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'pubkey', 'raddress']


class LocationSerializer(BaseWalletSerializer):
    # organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'pubkey', 'raddress', 'organization']


class BatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Batch
        fields = ['id', 'name', 'pubkey', 'raddress']


class PoolPurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PoolPurchaseOrder
        fields = ['id', 'name', 'pubkey', 'raddress']


class PoolBatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PoolBatch
        fields = ['id', 'name', 'pubkey', 'raddress']


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class PoolPurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PoolPurchaseOrder.objects.all()
    serializer_class = PoolPurchaseOrderSerializer


class PoolBatchViewSet(viewsets.ModelViewSet):
    queryset = PoolBatch.objects.all()
    serializer_class = PoolBatchSerializer


router = routers.DefaultRouter()
router.register(r'api/v1/organization', OrganizationViewSet)
# router.register(r'api/v1/organization/(?P<raddress>)', OrganizationViewSet)
# router.register(r'api/v1/organization/<str:raddress>/certificate', CertificateViewSet)
# router.register(r'api/v1/organization/(?P<id>[0-9a-f-]+)/location', LocationViewSet)
# router.register(r'api/v1/organization/(?P<raddress>[0-9a-f-]+)/location', LocationViewSet)
# router.register(r'api/v1/organization/<uuid:id>/batch', BatchViewSet)
# router.register(r'api/v1/organization/<uuid:id>/poolpo', PoolPurchaseOrderViewSet)
# router.register(r'api/v1/organization/<uuid:id>/poolbatch', PoolBatchViewSet)
