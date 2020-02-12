from django.shortcuts import render
from rest_framework import viewsets
from .models import StoredResult, ScrapedCustomResult, ScrapedResult
from .serializers import StoredResultSeralizer, ScrapedResultSerializer, ScrapedCustomResultSerialzer

class StoredResultView(viewsets.ModelViewSet):
    queryset = StoredResult.objects.all()
    serializer_class = StoredResultSeralizer

class ScrapedResultView(viewsets.ModelViewSet):
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer

class ScrapedCustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedCustomResult.objects.all()
    serializer_class = ScrapedCustomResultSerialzer