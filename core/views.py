from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ExperienceSerializer, EducationSerializer, LinkSerializer, ProfileSerializer
from rest_framework import status, viewsets
from rest_framework import generics
from .models import Experience, Education, Link, Profile
from rest_framework.response import Response
# Create your views here.



class ExperienceListCreate(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class ExperienceRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if not serializer.is_valid():
            return Response({'error': serializer.error}, status=422)
        serializer.save()
        return Response(serializer.data)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ProfileListCreate(generics.ListCreateAPIView):

class education(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class link(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer