from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Stored', views.StoredResultView)
router.register('Scraped', views.ScrapedResultView)
router.register('ScrapedCustom', views.ScrapedCustomResultView)

urlpatterns = [
    path('', include(router.urls))
]