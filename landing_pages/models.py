from django.db import models

# Create your models here.
class Tour(models.Model):
    name            = models.TextField(max_length=150)
    email           = models.TextField(max_length=150)



    def __str__(self):
        return self.name