from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country =models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class FoodPlace(models.Model):
    destination = models.ForeignKey(Destination, related_name="food_places", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{"self.name"} ({self.cuisine})"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_cuisine = models.CharField(max_length =100, blank=True, null=True)
    preferred_country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username



# Create your models here.
