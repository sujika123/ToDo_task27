from django.db import models

# Create your models here.
class task(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    Status = models.IntegerField(default=0)


