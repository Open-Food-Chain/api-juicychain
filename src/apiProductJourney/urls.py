from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('transactionid', views.TransactionidView)
router.register('walletaddress', views.WalletaddressView)
# router.register('productjourney', views.ProductjourneyView)
router.register('organization', views.OrganizationView)
router.register('batchdetail', views.BatchdetailView)
router.register('facility', views.FacilityView)
router.register('certificate', views.CertificateView)

urlpatterns = [
    path('', include(router.urls))
]
