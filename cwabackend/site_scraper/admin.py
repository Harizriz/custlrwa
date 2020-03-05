from django.contrib import admin
from .models import ScrapedResult, ScrapedCustomResult, Sizing, ProductPage, ImageUrl, Reviews
# Register your models here.
# admin.site.register(StoredResult)
admin.site.register(Sizing)
admin.site.register(ScrapedResult)
admin.site.register(ScrapedCustomResult)
admin.site.register(ImageUrl)
admin.site.register(Reviews)