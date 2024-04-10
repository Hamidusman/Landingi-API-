from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ExperienceSerializer, EducationSerializer
from rest_framework import status
from rest_framework import generics
from .models import Experience, Education
from rest_framework.response import Response
# Create your views here.



class experience(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class education(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer