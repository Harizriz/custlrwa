from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('Stored', views.StoredResultView)
# router.register('Scraped', views.ScrapedResultView)
router.register('ScrapedCustom', views.ScrapedCustomResultView)
router.register('Sizing', views.SizingView)

urlpatterns = [
    # path('', include(router.urls)),
    path('scraped/', views.ScrapedResultAPIView.as_view()),
    path('images/', views.ImageListAPIView.as_view()),
    path('reviews/', views.ReviewsAPIView.as_view())
]