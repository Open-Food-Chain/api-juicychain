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


class CertificateSerializer(BaseWalletSerializer):

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'date_issue', 'date_expiry', 'issuer', 'identifier', 'pubkey', 'raddress', 'organization']


class LocationSerializer(BaseWalletSerializer):
    # works
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


# Nested Serializer


class NestedLocationSerializer(serializers.HyperlinkedModelSerializer):
    # organization = OrganizationSerializer()

    class Meta:
        model = Location
        exclude = ['url', 'organization']
        # fields = '__all__'


class NestedCertificateSerializer(serializers.HyperlinkedModelSerializer):
    # organization = OrganizationSerializer()

    class Meta:
        model = Certificate
        exclude = ['url', 'organization']
        # fields = '__all__'


class NestedOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    location = NestedLocationSerializer(many=True)
    certificate = NestedCertificateSerializer(many=True)

    class Meta:
        model = Organization
        depth = 3
        fields = ['id', 'name', 'pubkey', 'raddress', 'location', 'certificate']


# Standalone ViewSet
##################################


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


# Nested ViewSet
#################################


class NestedOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = NestedOrganizationSerializer


router = routers.DefaultRouter()
router.register(r'api/v1/organization', OrganizationViewSet)
router.register(r'api/v1/organization-detail', NestedOrganizationViewSet, basename='organization-detail')
router.register(r'api/v1/location', LocationViewSet)
router.register(r'api/v1/certificate', CertificateViewSet)
# router.register(r'api/v1/organization/(?P<raddress>)', OrganizationViewSet)
# router.register(r'api/v1/organization/<str:raddress>/certificate', CertificateViewSet)
# router.register(r'api/v1/organization/(?P<id>[0-9a-f-]+)/location', LocationViewSet)
router.register(r'api/v1/organization/(?P<id>\d+)/location', LocationViewSet)
router.register(r'api/v1/organization/(?P<id>\d+)/certificate', CertificateViewSet)
# TODO works for id as integer, for UUID needs test
# router.register(r'api/v1/organization-detail/(?P<id>[0-9a-f]+)/location', LocationViewSet)
# router.register(r'api/v1/organization/(?P<raddress>[0-9a-f-]+)/location', LocationViewSet)
# router.register(r'api/v1/organization/<uuid:id>/batch', BatchViewSet)
# router.register(r'api/v1/organization/<uuid:id>/poolpo', PoolPurchaseOrderViewSet)
# router.register(r'api/v1/organization/<uuid:id>/poolbatch', PoolBatchViewSet)