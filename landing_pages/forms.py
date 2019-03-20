from django.forms import ModelForm
from .models import Tour

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'email','tour_date']