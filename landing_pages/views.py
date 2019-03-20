from django.shortcuts import render

# Create your views here.



# Home Page
def home_page(request):
    return render(request, 'landing_pages/home.html')


# Golden Gate Bridge Tour Page

def golden_gate_bridge(request):
    return render(request,'landing_pages/golden_gate_bridge.html')


# Contact Page

def contact(request):
    return render(request, 'landing_pages/contact.html')