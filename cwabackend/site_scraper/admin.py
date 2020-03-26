from django.contrib import admin
from .models import ScrapedResult, CustomSizing, Sizing, ImageUrl, Reviews
# Register your models here.
admin.site.register(Sizing)
admin.site.register(ScrapedResult)
admin.site.register(CustomSizing)
admin.site.register(ImageUrl)
admin.site.register(Reviews)