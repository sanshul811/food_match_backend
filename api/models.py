from django.db import models

# Create your models here.
# myapp/models.py

class CaffePost(models.Model):
    user = models.CharField(max_length=200)
    name = models.TextField()
    
