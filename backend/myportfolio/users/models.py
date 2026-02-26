from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
