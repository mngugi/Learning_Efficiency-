# research/views.py
from rest_framework import viewsets, serializers
from django.shortcuts import render
from .models import LearningSession

# Serializer for your LearningSession model
class LearningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSession
        fields = '__all__'

# DRF ViewSet for CRUD operations
class LearningSessionViewSet(viewsets.ModelViewSet):
    queryset = LearningSession.objects.all()
    serializer_class = LearningSessionSerializer

# Homepage view
def home(request):
    return render(request, "index.html")