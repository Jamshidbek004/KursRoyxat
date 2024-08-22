from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from app.views import RoyxatViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Router
router = DefaultRouter()
router.register(r'royxat', RoyxatViewSet, basename='royxat')

# Swagger uchun schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Royxat API",
      default_version='v1',
      description="Bu API ro'yxat ma'lumotlari bilan ishlash uchun mo'ljallangan",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jamshidbekxaminov17@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# URL konfiguratsiya
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
