from django.forms import ModelForm
from .models import Tour
from django import forms




class TourForm(ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': "i.e. Olivia Lee "
    }
    ))

    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': "i.e. Olivia@gmail.com"
    }
    ))

    tour_date = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': "i.e. 07/07/2019 - 10AM"
    }
    ))

    number_of_people  = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': "i.e. 3 people"
    }))

    class Meta:
        model = Tour
        fields = ['name', 'email','tour_date','number_of_people']