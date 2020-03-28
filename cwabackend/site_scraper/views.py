from django.shortcuts import render
from rest_framework import viewsets, filters, generics, pagination
from .models import CustomSizing, ScrapedResult, Sizing, ImageUrl, Reviews
from .serializers import ScrapedResultSerializer, CustomResultSerializer, SizingSerializer, ReviewsSerializer, BrandListSerializer

class ReviewsPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class ResultPagination (pagination.PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 240

class LargePagination (pagination.PageNumberPagination):
    page_size = 5000
    page_size_query_param = 'page_size'
    max_page_size = 10000

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
            self.pagination_class = LargePagination
            self.serializer_class = BrandListSerializer
            
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
    pagination_class = ResultPagination
    http_method_names = ['get']

class ReviewsAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = ReviewsPagination
    http_method_names = ['get', 'post']

class CustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedResult.objects.all()
    serializer_class = CustomResultSerializer
    pagination_class = ResultPagination
    http_method_names = ['get']