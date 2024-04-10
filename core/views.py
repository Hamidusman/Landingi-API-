from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ExperienceSerializer
from rest_framework import status
from rest_framework import generics
from .models import Experience
from rest_framework.response import Response
# Create your views here.



class experience(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer