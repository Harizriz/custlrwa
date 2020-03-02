from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import ScrapedCustomResult, ScrapedResult, Sizing
from .serializers import ScrapedResultSerializer, ScrapedCustomResultSerialzer, SizingSerializer

# class StoredResultView(viewsets.ModelViewSet):
#     queryset = StoredResult.objects.all()
#     serializer_class = StoredResultSeralizer

# class ScrapedResultView(viewsets.ModelViewSet):
#     queryset = ScrapedResult.objects.all()
#     serializer_class = ScrapedResultSerializer

class ScrapedResultAPIView(generics.ListCreateAPIView):
    search_fields = ['product_name', 'brand']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer

class ScrapedCustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedCustomResult.objects.all()
    serializer_class = ScrapedCustomResultSerialzer

class SizingView(viewsets.ModelViewSet):
    queryset = Sizing.objects.all()
    serializer_class = SizingSerializer
