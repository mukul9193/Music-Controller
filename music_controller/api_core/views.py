from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import RoomSerializers # type: ignore

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers   # type: ignore
    
    