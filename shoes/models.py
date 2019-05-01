from django.db import models

# Create your models here.
class Shoe(models.Model):
    size    = models.TextField(max_length=300)
    color   = models.TextField(max_length=500)