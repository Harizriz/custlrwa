from django.db import models

# Create your models here.
class StoredResult(models.Model):
    product_name = models.TextField(null = True)
    sizing = models.CharField(null = True, max_length = 5) #for sizes like xxxxl
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)

class ScrapedResult(models.Model):
    product_name = models.TextField(null = True)
    sizing = models.CharField(null = True, max_length = 5) #for sizes like xxxxl
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)

class ScrapedCustomResult(models.Model):
    product_name = models.TextField(null = True)
    #sizing = #still figuring out how to create a custom field for sizing
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)