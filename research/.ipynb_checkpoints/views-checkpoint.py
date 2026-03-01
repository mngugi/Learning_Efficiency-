from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import LearningSession

# Serializer
class LearningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSession
        fields = '__all__'

# ViewSet
class LearningSessionViewSet(viewsets.ModelViewSet):
    queryset = LearningSession.objects.all()
    serializer_class = LearningSessionSerializer

# Simple home view
def home(request):
    return render(request, "index.html")