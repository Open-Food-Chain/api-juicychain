from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from django.core.validators import RegexValidator
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from lib import juicychain
from .models import (
    Organization,
    Certificate,
    CertificateRule,
    Location,
    Batch,
    PoolPurchaseOrder,
    PoolBatch,
    KV
)
from .lib import openfood
import json

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


class KvSerializer(serializers.ModelSerializer):
	key = serializers.CharField(
	max_length=66 )
	keylen = serializers.CharField(
	max_length=255 )
	
	class Meta:
		model = KV
		fields = ['key', 'keylen']


class CertificateSerializer(BaseWalletSerializer):

    # rule = CertificateRuleSerializer(many=True)
    pubkey = serializers.CharField(allow_blank=True)
    raddress = serializers.CharField(allow_blank=True)

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'date_issue', 'date_expiry', 'issuer', 'identifier', 'pubkey', 'raddress', 'txid_funding', 'organization']


class CertificateRuleSerializer(BaseWalletSerializer):
    # id = serializers.UUIDField(read_only=True)

    pubkey = serializers.CharField(allow_blank=True)
    raddress = serializers.CharField(allow_blank=True)

    class Meta:
        model = CertificateRule
        fields = ['id', 'name', 'condition', 'pubkey', 'raddress', 'certificate']


class LocationSerializer(BaseWalletSerializer):
    # works
    # organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'pubkey', 'raddress', 'organization']


class BatchSerializer(BaseWalletSerializer):

    pubkey = serializers.CharField(allow_blank=True)
    raddress = serializers.CharField(allow_blank=True)

    class Meta:
        model = Batch
        fields = ['id', 'identifier', 'jds', 'jde', 'date_production_start', 'date_best_before', 'delivery_date', 'origin_country', 'pubkey', 'raddress', 'organization']


class PoolPurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PoolPurchaseOrder
        fields = ['id', 'name', 'pubkey', 'raddress']


class PoolBatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PoolBatch
        fields = ['id', 'name', 'pubkey', 'raddress']


# Nested Serializer


class NestedBatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Batch
        exclude = ['url', 'organization']


class NestedCertificateRuleSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.UUIDField(read_only=True)

    class Meta:
        model = CertificateRule
        exclude = ['url', 'certificate']


class NestedLocationSerializer(serializers.HyperlinkedModelSerializer):
    # organization = OrganizationSerializer()

    class Meta:
        model = Location
        exclude = ['url', 'organization']
        # fields = '__all__'


class NestedCertificateSerializer(serializers.HyperlinkedModelSerializer):
    rule = NestedCertificateRuleSerializer(many=True)

    class Meta:
        model = Certificate
        exclude = ['url', 'organization']
        # fields = '__all__'


class NestedOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    location = NestedLocationSerializer(many=True)
    certificate = NestedCertificateSerializer(many=True)
    batch = NestedBatchSerializer(many=True)

    class Meta:
        model = Organization
        depth = 3
        fields = ['id', 'name', 'pubkey', 'raddress', 'location', 'certificate', 'batch']


# Standalone ViewSet
##################################


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def patch(self, request, *args, **kwargs):
        juicychain.connect_node()
        data = {"mylo": "testing123"}
        kv_response = juicychain.kvupdate_wrapper("mylokv1", data, "1", "mylo")
        return Response(kv_response, status=status.HTTP_201_CREATED)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    @action(detail=False)  # listview
    def noraddress(self, request, pk=None):
        no_raddress = Certificate.objects.filter(
            raddress__exact=''
        )
        serializer = self.get_serializer(no_raddress, many=True)
        return Response(serializer.data)


class CertificateRuleViewSet(viewsets.ModelViewSet):
    queryset = CertificateRule.objects.all()
    serializer_class = CertificateRuleSerializer

    @action(detail=False)  # listview
    def noraddress(self, request, pk=None):
        no_raddress = CertificateRule.objects.filter(
            raddress__exact=''
        )
        serializer = self.get_serializer(no_raddress, many=True)
        return Response(serializer.data)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# class proxyKV():
#	key = ""
#	value = ""
#
#	def __init__(self, iKey, iValue):
#		self.key = iKey
#		self.value = iValue


class KvViewSet(viewsets.ModelViewSet):
    queryset = KV.objects.none()
    serializer_class = KvSerializer	
    openfood.connect_node()

    def get_queryset(self):
        print("KV")
        key = self.request.query_params.get('key', None)
        if not key:
            key = "mylo"
        value = openfood.kvsearch_wrapper(key)
        print(value)
        if 'value' not in value:
            return KV.objects.none()
        return value


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    print("HERE")

    def get_queryset(self):
        print("CHCKING")
        queryset = Batch.objects.all()
        bbd = self.request.query_params.get('bbd', None)
        jds = self.request.query_params.get('jds', None)
        if (bbd is not None) and (jds is not None):
            # TODO find better querying techniques
            queryset = queryset.filter(date_best_before=bbd, jds=jds)[0:1]
        return queryset


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
router.register(r'api/v1/certificate-rule', CertificateRuleViewSet)
router.register(r'api/v1/batch', BatchViewSet)
router.register(r'api/v1/kv', KvViewSet)
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
# did not work
# router.register(r'api/v1/certificate-new', CertificateViewSet.as_view({'get': 'no_raddress'}), basename='certificate-new')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/certificate-new/', CertificateViewSet.as_view({'get': 'noraddress'})),
    path('api/v1/certificate-rule-new/', CertificateRuleViewSet.as_view({'get': 'noraddress'}))
]

