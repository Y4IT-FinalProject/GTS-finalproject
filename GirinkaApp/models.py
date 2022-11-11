from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Announcements(models.Model):
    title=models.CharField(max_length=255)
    published_date=models.DateField()
    expired_date=models.DateField()
    location=models.CharField(max_length=100)
    posted_by=models.CharField(max_length=100)
    attachment = models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.title

    