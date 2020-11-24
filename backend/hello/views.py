from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HelloSerializer
from .models import Hello                   

class HelloView(viewsets.ModelViewSet):
  serializer_class = HelloSerializer
  queryset = Hello.objects.all()
