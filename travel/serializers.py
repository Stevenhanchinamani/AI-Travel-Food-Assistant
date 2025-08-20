from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Destination, FoodPlace, UserProfile

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination   #  Tell DRF which model
        fields = '__all__'    #  Include all model fields


class FoodPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlace
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ["user", "favorite_cuisine","preferred_country"]
        