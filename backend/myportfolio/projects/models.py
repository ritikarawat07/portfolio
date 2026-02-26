# projects/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    tech_stack = models.CharField(max_length=250)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title