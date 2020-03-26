from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('page', views.ScrapedResultView)
# router.register('ScrapedCustom', views.ScrapedCustomResultView)

urlpatterns = [
    path('', include(router.urls)),
    path('scraped/', views.ScrapedResultAPIView.as_view()),
    path('reviews/', views.ReviewsAPIView.as_view()),
]