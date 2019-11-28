from django.contrib import admin
from .models import StoredResult, ScrapedResult, ScrapedCustomResult
# Register your models here.
admin.site.register(StoredResult)
admin.site.register(ScrapedResult)
admin.site.register(ScrapedCustomResult)