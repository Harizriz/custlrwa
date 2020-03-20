from django.db import models

# Create your models here.
class ScrapedResult(models.Model):
    id = models.BigIntegerField(primary_key = True, null = False)
    product_name = models.TextField(null=True)
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)
    product_description = models.TextField(null=True)
    original_site = models.TextField(null=True)
    category = models.TextField(null=True)
    subcategory = models.TextField(null=True)

class Sizing(models.Model):
    sizing = models.CharField(max_length = 10, null = True)
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True)

class ImageUrl(models.Model):
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True)
    image_url = models.TextField()

class Reviews(models.Model):
    product = models.ForeignKey(ScrapedResult, on_delete=models.CASCADE, null = True)
    reviewer_name = models.TextField()
    summary = models.TextField(max_length=50)
    review = models.TextField(max_length=300)
    quality = models.IntegerField()
    price = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.product_id
    
    class Meta:
        ordering = ['product_id']

class ScrapedCustomResult(models.Model):
    product_name = models.TextField(null = True)
    # TODO Make custom sizing a foreign key table
    chest_size = models.FloatField(null = True)
    waist_size = models.FloatField(null = True)
    sleeve_length = models.FloatField(null = True)
    shoulder_size = models.FloatField(null = True)
    neck_size = models.FloatField(null = True)
    arm_size = models.FloatField(null = True)
    
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)
