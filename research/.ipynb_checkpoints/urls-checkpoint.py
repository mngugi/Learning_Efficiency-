from rest_framework.routers import DefaultRouter
from .views import LearningSessionViewSet

router = DefaultRouter()
router.register(r'sessions', LearningSessionViewSet)

urlpatterns = router.urls