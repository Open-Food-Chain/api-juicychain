from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('certificate', views.CertificateView)
router.register('certificate-conditions', views.CertificateConditionsView)

urlpatterns = [
    path('', include(router.urls))
]
