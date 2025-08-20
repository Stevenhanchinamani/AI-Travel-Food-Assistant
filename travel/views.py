from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination, FoodPlace
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import DestinationSerializer, FoodPlaceSerializer, UserProfileSerializer

@api_view(['GET'])
def destinations_list(request):
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_destination(request):
    serializer = DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#New: List all food places

@api_view(["GET"])
def food_places_list(request):
    food_places = FoodPlace.objects.all()
    serializer = FoodPlaceSerializer(food_places, many=True)
    return Response(serializer.data)


#New: Add a new food place
@api_view(["POST"])
def add_food_place(request):
    serializer = FoodPlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# Recommendation (AI/ML stub for now)

@api_view(["GET"])
def recommend_food(request, destination_id):
    """
    AI-Powered recommendation using cosine similarity (stub version)
    
    """
    destination = get_object_or_404(Destination, id=destination_id)

    # TODO: Replace this with ML later
    recommended_places = FoodPlace.objects.filter(destination=destination)

    serializer = FoodPlaceSerializer(recommended_places, many=True)
    return Response({
        "destination":destination.name,
        "recommended_food_places": serializer.data
    })


@api_view(["POST"])
def create_user_profile(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.create_user(username=username, email=email, password=password)
    profile = UserProfile.objects.create(user=user)   

    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, status=201)


@api_view(["GET"])
def get_user_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user_id=user_id)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)


# Based on User Profile
@api_view(["GET"])
def personalized_recommendation(request, user_id):   
    profile = get_object_or_404(UserProfile, user_id=user_id)

    # filter food places by user's favorite cuisine or country
    food_places = FoodPlace.objects.all()
    if profile.favorite_cuisine:
        food_places = food_places.filter(cuisine__icontains=profile.favorite_cuisine)  # ✅ fixed

    if profile.preferred_country:
        food_places = food_places.filter(destination__country__icontains=profile.preferred_country)  # ✅ fixed

    serializer = FoodPlaceSerializer(food_places, many=True)
    return Response({
        "user": profile.user.username,
        "preferences": {
            "favorite_cuisine": profile.favorite_cuisine,
            "preferred_country": profile.preferred_country
        },
        "personalized_recommendations": serializer.data
    })
    
# Create your views here.
