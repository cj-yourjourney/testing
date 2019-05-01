from django.db import models
from django.utils import timezone




# Create your models here.
class Tour(models.Model):
    name            = models.CharField(max_length=150)
    email           = models.CharField(max_length=150)
    tour_date       = models.CharField(max_length=150)
    number_of_people  = models.CharField(max_length=150)



    def __str__(self):
        return '{} - {}'.format(self.name, self.tour_date)