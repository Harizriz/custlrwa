"""
Registering models for backed
Done by Gerald
"""

from django.contrib import admin
from .models import ScrapedResult, Sizing, ImageUrl, Reviews
# Register your models here.
admin.site.register(Sizing)
admin.site.register(ScrapedResult)
admin.site.register(ImageUrl)
admin.site.register(Reviews)