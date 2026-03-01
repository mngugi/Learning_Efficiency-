from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LearningSessionViewSet, home

# DRF router
router = DefaultRouter()
router.register(r'sessions', LearningSessionViewSet, basename='sessions')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # /api/sessions/
    path('', home, name='home'),        # homepage
]