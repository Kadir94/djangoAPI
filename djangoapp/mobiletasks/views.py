from django.shortcuts import render
from rest_framework import viewsets
from .models import Stations
from .serializers import StationSerializers



class StationView(viewsets.ModelViewSet):
    filterset_fields = ('latitude','longnitude')
    serializer_class = StationSerializers
    queryset = Stations.objects.all().order_by('station_name')






