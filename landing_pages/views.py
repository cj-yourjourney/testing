from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'landing_pages/home.html')