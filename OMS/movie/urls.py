from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views


router = DefaultRouter()

router.register('titles', views.MovieViewSet)
router.register('titles/rent', views.RentViewSet)
router.register('rental/return', views.ReturnViewSet)
router.register('rental/price', views.PriceViewSet)

app_name = 'movie'

urlpatterns = [
    path('', include(router.urls))
]