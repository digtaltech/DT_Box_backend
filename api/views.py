from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Data
from django.contrib.auth.models import User
from .serializer import UserSerializer, DataSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class DataViewSet(viewsets.ModelViewSet):

    serializer_class = DataSerializer
    def get_queryset(self):

        user = self.request.user
        queryset = Data.objects.filter(username=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
