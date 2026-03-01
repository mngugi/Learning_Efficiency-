from django.urls import path
from .views import LearningSessionViewSet, home  # import your views

urlpatterns = [
    # Example home page
    path('', home, name='home'),

    # Example API endpoint
    path('api/sessions/', LearningSessionViewSet.as_view({'get': 'list'}), name='sessions-list'),
]