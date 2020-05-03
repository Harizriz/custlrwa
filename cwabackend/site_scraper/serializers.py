from rest_framework import serializers
from .models import ScrapedResult, CustomSizing, Sizing, ImageUrl, Reviews

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedResult
        fields = ('brand',)

class SizingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizing
        fields = ('sizing',)

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUrl
        fields = ('image_url',)

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('product', 'reviewer_name', 'summary', 'review', 'quality', 'price', 'value')

class ScrapedResultSerializer(serializers.ModelSerializer):
    imagelist = ImageListSerializer(source ='images', many=True, required=False)
    sizing = SizingSerializer(many=True, required=False)

    class Meta:
        model = ScrapedResult
        fields = ('id', 'product_name', 'price', 'currency', 'brand', 'image_url', 'product_description', 'original_site', 'category', 'subcategory', 'imagelist', 'sizing', 'sizing_type', 'occasion')

class CustomSizingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSizing
        fields = ('product', 'chest_size', 'waist_size', 'sleeve_length', 'shoulder_size', 'neck_size', 'arm_size')

class CustomResultSerializer(serializers.ModelSerializer):
    imagelist = ImageListSerializer(source ='images', many=True, required=False)
    sizing = CustomSizingSerializer(required=False)

    class Meta:
        model = ScrapedResult
        fields = ('id', 'product_name', 'price', 'currency', 'brand', 'image_url', 'product_description', 'original_site', 'category', 'subcategory', 'imagelist', 'sizing')