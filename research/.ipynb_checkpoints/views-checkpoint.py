from rest_framework import viewsets
from .models import LearningSession
from .serializers import LearningSessionSerializer

class LearningSessionViewSet(viewsets.ModelViewSet):
    queryset = LearningSession.objects.all().order_by('-created_at')
    serializer_class = LearningSessionSerializer