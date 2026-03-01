from django.db import models

class LearningSession(models.Model):
    title = models.CharField(max_length=255)
    time_spent = models.FloatField()          # Ts
    concept_links = models.FloatField()       # Cl
    knowledge_gaps = models.FloatField()      # Kg
    research_questions = models.FloatField()  # Rq
    learning_efficiency = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title