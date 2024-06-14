# models.py in your Django app (e.g., health_app)
from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()

    def __str__(self):
        return self.name
