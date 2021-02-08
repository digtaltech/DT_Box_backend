from rest_framework import serializers
from .models import Data
from django.contrib.auth.models import User

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def save(self):
#
#         account = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#         password = self.validated_data['password']
#         account.set_password(password)
#         account.save()
#         return account


class UserSerializer(serializers.ModelSerializer):
    datas = serializers.PrimaryKeyRelatedField(many=True, queryset=Data.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tours']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    # places = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Data
        fields = ['id','username', 'sessionId', 'data']

    # def create(self, validated_data):
    #     days_data = validated_data.pop('days')
    #     tour = Tour.objects.create(**validated_data)
    #     for day_data in days_data:
    #         places_data = day_data.pop('places')
    #         day = Day.objects.create(tour=tour, **day_data)
    #         for place_data in places_data:
    #             Place.objects.create(day=day, **place_data)
    #     return tour
