from django.shortcuts import render
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "Ok", "message": "API is healthy"})

# Create your views here.
