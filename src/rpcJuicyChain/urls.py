from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('getinfo', views.getinfo)

urlpatterns = [
    path('getinfo', views.getinfo, name='getinfo')
]
