from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from api.views import DataViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='user')

router.register('data', DataViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
