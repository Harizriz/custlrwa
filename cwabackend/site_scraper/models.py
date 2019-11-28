from django.db import models

# Create your models here.
class StoredResult(models.Model):
    product_name = models.TextField()
    sizing = models.CharField(max_length = 5) #for sizes like xxxxl
    price = models.FloatField()
    currency = models.CharField(max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(max_length = 50)
    image_url = models.URLField(NULL = True, max_length = 300)

class ScrapedResult(model.Model):
    product_name = models.TextField()
    sizing = models.CharField(max_length = 5) #for sizes like xxxxl
    price = models.FloatField()
    currency = models.CharField(max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(max_length = 50)
    image_url = models.URLField(NULL = True, max_length = 300)

class ScrapedCustomResult(model.Model):
    product_name = models.TextField()
    # sizing =  #still researching how to create a custom field for this
    price = models.FloatField()
    currency = models.CharField(max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(max_length = 50)
    image_url = models.URLField(NULL = True, max_length = 300)