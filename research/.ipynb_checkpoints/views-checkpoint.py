# research/views.py
from rest_framework import viewsets
from rest_framework import serializers
from .models import LearningSession
from django.shortcuts import render

# --- DRF Serializer ---
class LearningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSession
        fields = '__all__'

# --- ViewSet for DRF ---
class LearningSessionViewSet(viewsets.ModelViewSet):
    queryset = LearningSession.objects.all()
    serializer_class = LearningSessionSerializer

# --- Simple homepage ---
def home(request):
    return render(request, "index.html")