from django.db import models

# Create your models here.
class Sizing(models.Model):
    code = models.CharField(null = True, max_length = 5)
    description = models.CharField(null = True, max_length = 10)
    
    def __str__(self):
        return self.description

class ImageUrl(models.Model):
    product_id = models.IntegerField()
    image_url = models.TextField()

    def __str__(self):
        return self.product_id
    
    class Meta:
        ordering = ['product_id']

class Reviews(models.Model):
    product_id = models.IntegerField()
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

class ProductPage(models.Model):
    product_name = models.TextField(null=True)
    curency = models.CharField(null=True, max_length=5)
    price = models.FloatField(null=True)
    images_id = models.ForeignKey(ImageUrl, on_delete=models.CASCADE, null = True)
    product_description = models.TextField(null=True)
    reviews_id = models.ForeignKey(Reviews, on_delete=models.CASCADE, null = True)
    original_site = models.TextField(null=True)

    def __str__(self):
        return self.product_name

# class StoredResult(models.Model):
#     product_name = models.TextField(null = True)
#     sizing = models.CharField(null = True, max_length = 5) #for sizes like xxxxl
#     price = models.FloatField(null = True)
#     currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
#     brand = models.CharField(null = True, max_length = 50)
#     image_url = models.URLField(null = True, max_length = 300)

class ScrapedResult(models.Model):
    product_name = models.OneToOneField(ProductPage, on_delete=models.CASCADE, null = True)
    sizing = models.ForeignKey(Sizing, on_delete=models.CASCADE, null = True)
    price = models.FloatField(null = True)
    currency = models.CharField(null = True, max_length = 3) #currency like USD, MYR, JPY, THB, etc.
    brand = models.CharField(null = True, max_length = 50)
    image_url = models.URLField(null = True, max_length = 300)
     
    def __str__(self):
        return self.product_name
    

class ScrapedCustomResult(models.Model):
    product_name = models.TextField(null = True)
    #sizing will no longer be a single field for custom result search, as the logic for that is too much of a hassle when dealing with NoSQL and Django Fields
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
