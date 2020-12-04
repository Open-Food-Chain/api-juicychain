from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('getinfo', views.getinfo)

urlpatterns = [
    path('kvupdate1', views.kvupdate1, name='kvupdate1')
]
