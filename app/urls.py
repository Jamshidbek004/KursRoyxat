from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoyxatViewSet

router = DefaultRouter()
router.register(r'royxat', RoyxatViewSet, basename='royxat')

urlpatterns = [
    path('', include(router.urls)),
]
