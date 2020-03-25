from django.shortcuts import render
from rest_framework import viewsets, filters, generics, pagination
from .models import ScrapedCustomResult, ScrapedResult, Sizing, ImageUrl, Reviews
from .serializers import ScrapedResultSerializer, ScrapedCustomResultSerialzer, SizingSerializer, ImageListSerializer, ReviewsSerializer

class PaginationDefault (pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 125

class ResultPagination (pagination.PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 240

class ScrapedResultAPIView(generics.ListCreateAPIView):
    search_fields = ['product_name', 'brand', 'product_description', 'category', 'subcategory']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer
    pagination_class = ResultPagination
    http_method_names = ['get']

    def get_queryset(self):
        category = self.request.query_params.get('category')
        brand = self.request.query_params.get('brand')
        maxprice = self.request.query_params.get('maxprice')
        minprice = self.request.query_params.get('minprice')
        brandlist = self.request.query_params.get('brandlist')
        queryset = ScrapedResult.objects

        if brandlist == 'true':
            queryset = queryset.distinct('brand')

            
        queryset = queryset.all()

        if category != None:
            queryset = queryset.filter(category__iexact=category)
        if brand != None:
            queryset = queryset.filter(brand__iexact=brand)
        if maxprice == None or minprice == None:
            maxprice = 100000
            minprice = 0
        
        queryset = queryset.filter(price__gte=minprice, price__lte=maxprice)
        
        return queryset

class ScrapedResultView(viewsets.ModelViewSet):
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class SizingAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Sizing.objects.all()
    serializer_class = SizingSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class ImageListAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = ImageUrl.objects.all()
    serializer_class = ImageListSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class ReviewsAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get', 'post']

class ScrapedCustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedCustomResult.objects.all()
    serializer_class = ScrapedCustomResultSerialzer
    http_method_names = ['get']