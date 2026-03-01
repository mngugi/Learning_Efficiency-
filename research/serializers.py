from rest_framework import serializers
from .models import LearningSession
from .services import calculate_learning_efficiency

class LearningSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningSession
        fields = '__all__'
        read_only_fields = ['learning_efficiency']

    def create(self, validated_data):
        efficiency = calculate_learning_efficiency(
            validated_data['time_spent'],
            validated_data['concept_links'],
            validated_data['knowledge_gaps'],
            validated_data['research_questions']
        )

        validated_data['learning_efficiency'] = efficiency
        return super().create(validated_data)