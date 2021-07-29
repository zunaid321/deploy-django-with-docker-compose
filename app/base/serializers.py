from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['type', 'heading', 'id']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['heading', 'id']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'