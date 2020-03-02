from rest_framework import serializers
from .models import ScrapedResult, ScrapedCustomResult, Sizing

# class StoredResultSeralizer(serializers.ModelSerializer):
#     class Meta:
#         model = StoredResult
#         fields = ('id', 'product_name', 'sizing', 'price', 'currency', 'brand', 'image_url')

class ScrapedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedResult
        fields = ('id', 'product_name', 'sizing', 'price', 'currency', 'brand', 'image_url')

class ScrapedCustomResultSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedCustomResult
        fields = ('id', 'product_name', 'chest_size', 'waist_size', 'sleeve_length', 'shoulder_size', 'neck_size', 'arm_size', 'price', 'currency', 'brand', 'image_url')

class SizingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizing
        fields = ('code', 'description')