import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class GraduationYear(models.Model):
    graduationYear_text = models.CharField(max_length=4)
    # ...
    def __str__(self):
        return self.graduationYear_text

# Distinguished Graduates pulled from https://www.usma.edu/about/history-of-west-point/notable-graduates
class DistinguishedGraduates(models.Model):
    graduationYear = models.ForeignKey(GraduationYear, on_delete=models.CASCADE)
    graduate_text = models.CharField(max_length=200)
    # ...
    def __str__(self):
        return self.graduate_text
