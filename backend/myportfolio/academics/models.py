from django.db import models

class AcademicRecord(models.Model):
    level = models.CharField(max_length=50) # 10th, 12th, B.Tech etc.
    institution = models.CharField(max_length=255)
    percentage = models.FloatField()
    marksheet = models.FileField(upload_to='marksheets/')

    def __str__(self):
        return self.level
