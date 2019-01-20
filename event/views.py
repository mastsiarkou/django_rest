from django.shortcuts import render

from .models import Timer
from .serializers import TimerSerializer
from rest_framework import generics


class TimerList(generics.ListCreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer