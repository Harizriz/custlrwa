from rest_framework import serializers
from .models import ScrapedResult, ScrapedCustomResult, Sizing, ImageUrl, Reviews

class ScrapedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedResult
        fields = ('id', 'product_name', 'sizing', 'price', 'currency', 'brand', 'image_url', 'product_description', 'original_site')

class ScrapedCustomResultSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedCustomResult
        fields = ('id', 'product_name', 'chest_size', 'waist_size', 'sleeve_length', 'shoulder_size', 'neck_size', 'arm_size', 'price', 'currency', 'brand', 'image_url')

class SizingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizing
        fields = ('product_id', 'description')

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUrl
        fields = ('product_id', 'image_url')

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('product_id', 'reviewer_name', 'summary', 'review', 'quality', 'price', 'value')