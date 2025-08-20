from django.urls import path
from .views import destinations_list, add_destination, food_places_list, add_food_place, recommend_food, create_user_profile, get_user_profile, personalized_recommendation
from .import views


urlpatterns = [
    path('destinations/', views.destinations_list, name='destinations_list'), #GET all destination
    path('destinations/add/', views.add_destination, name='add_destination'), #POST New destination
    path('destination/<int:destination_id>/food-places/', food_places_list),
    path('add-food-place/', add_food_place),
    path("recommend-food/<int:destination_id>/", recommend_food, name="recommend_food"),
    path("create-user/", create_user_profile, name="create-user"),
    path("user-profile/<int:user_id>/", get_user_profile, name="user-profile"),
    path("personalized-recommendations/<int:user_id>/", personalized_recommendation, name="personalized-recommendations"),
]


