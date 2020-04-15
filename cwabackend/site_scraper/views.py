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
    search_fields = ['product_name', 'brand', 'product_description', 'category', 'subcategory', 'original_site', 'occasion']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer
    pagination_class = ResultPagination
    http_method_names = ['get']

    def get_queryset(self):
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory')
        brand = self.request.query_params.get('brand')
        maxprice = self.request.query_params.get('maxprice')
        minprice = self.request.query_params.get('minprice')
        brandlist = self.request.query_params.get('brandlist')
        sizingtype = self.request.query_params.get('sizetype')
        occasion = self.request.query_params.get('occasion')

        uk_size = self.request.query_params.get('uk')
        us_size = self.request.query_params.get('us')
        eu_size = self.request.query_params.get('eu')
        intl_size = self.request.query_params.get('intl')
        size_qs = Sizing.objects
        queryset = ScrapedResult.objects

        if uk_size !=None and us_size !=None and eu_size !=None and intl_size !=None:
            qs_uk = size_qs.all().filter(sizing__iexact=uk_size)
            qs_us = size_qs.all().filter(sizing__iexact=us_size)
            qs_eu = size_qs.all().filter(sizing__iexact=eu_size)
            qs_intl = size_qs.all().filter(sizing__iexact=intl_size)

            '''
            A lot is happening underneath, first the 4 querysets for the different sizes are unified, 
            then all duplicate ids are removed, after that the other columns are filtered out, 
            leaving only the product id, which we will turn into a list for the ScrapedResult 
            queryset to filter by id with.
            '''
            id_list = list((qs_uk.union(qs_us, qs_eu, qs_intl)).distinct('product_id').values_list('product_id', flat=True))                 
            queryset = ScrapedResult.objects.filter(id__in = id_list)

        if brandlist == 'true':
            queryset = queryset.distinct('brand')
            self.pagination_class = LargePagination
            self.serializer_class = BrandListSerializer
            
        queryset = queryset.all()

        if subcategory != None:
            queryset = queryset.filter(subcategory__iexact=subcategory)
        if occasion != None:
            queryset = queryset.filter(occasion__iexact=occasion)
        if sizingtype != None:
            queryset = queryset.filter(sizing_type__iexact=sizingtype)
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
    http_method_names = ['get', 'post', 'delete']

class CustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedResult.objects.all()
    serializer_class = CustomResultSerializer
    pagination_class = ResultPagination
    http_method_names = ['get']