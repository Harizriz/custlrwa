from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import ScrapedCustomResult, ScrapedResult, Sizing, ImageUrl, Reviews
from .serializers import ScrapedResultSerializer, ScrapedCustomResultSerialzer, SizingSerializer, ImageListSerializer, ReviewsSerializer

class ScrapedResultAPIView(generics.ListCreateAPIView):
    search_fields = ['product_name', 'brand', 'product_description', 'category', 'subcategory']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer

class ScrapedCustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedCustomResult.objects.all()
    serializer_class = ScrapedCustomResultSerialzer

class SizingView(viewsets.ModelViewSet):
    queryset = Sizing.objects.all()
    serializer_class = SizingSerializer

class ImageListAPIView(generics.ListCreateAPIView):
    search_fields = ['product_id']
    filter_backends = (filters.SearchFilter,)
    queryset = ImageUrl.objects.all()
    serializer_class = ImageListSerializer

class ReviewsAPIView(generics.ListCreateAPIView):
    search_fields = ['product_id']
    filter_backends = (filters.SearchFilter,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer