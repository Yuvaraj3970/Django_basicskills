from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256)
    contact = models.PositiveBigIntegerField()
    interests = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    