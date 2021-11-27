from django.db import models

# Create your models here.
class Info(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Pass = models.CharField(max_length=300)
    Ads = models.TextField()
    City = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
