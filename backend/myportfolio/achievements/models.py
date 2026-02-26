# achievements/models.py
from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    year = models.IntegerField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title