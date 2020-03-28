from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ScrapedResult(models.Model):
    id = models.BigIntegerField(primary_key = True, null = False, unique=True)
    product_name = models.TextField(null=True)
    price = models.DecimalField(null = True, max_digits=9, decimal_places=2)
    currency = models.CharField(null = True, max_length = 10) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)
    product_description = models.TextField(null=True)
    original_site = models.TextField(null=True)
    category = models.TextField(null=True)
    subcategory = models.TextField(null=True)

class Sizing(models.Model):
    sizing = models.CharField(max_length = 20, null = True)
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True, related_name='sizing')

class ImageUrl(models.Model):
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True, related_name='images')
    image_url = models.TextField()

class Reviews(models.Model):
    product = models.ForeignKey(ScrapedResult, on_delete=models.DO_NOTHING, null = True)
    reviewer_name = models.TextField()
    summary = models.TextField(max_length=50)
    review = models.TextField(max_length=300)
    quality = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    value = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class CustomSizing(models.Model):
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True, related_name='custom_sizing')
    chest_size = models.FloatField(null = True)
    waist_size = models.FloatField(null = True)
    sleeve_length = models.FloatField(null = True)
    shoulder_size = models.FloatField(null = True)
    neck_size = models.FloatField(null = True)
    arm_size = models.FloatField(null = True)