from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
# Create your views here.

class ServiceListView(ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()

class ServiceDetailView(RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = "id"

class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()

class NewsDetailView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = "id"

class ClientListView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
