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
    path('Scraped/', views.ScrapedResultAPIView.as_view())
]