from django.db import models


class Academic(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    board_or_university = models.CharField(max_length=200)
    year_of_completion = models.IntegerField()
    percentage_or_cgpa = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.degree} - {self.institution}"