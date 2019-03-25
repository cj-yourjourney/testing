from django.shortcuts import render, redirect
from .forms import TourForm
from .models import Tour
# Create your views here.



# Home Page
def home_page(request):
    return render(request, 'landing_pages/home.html')


# Golden Gate Bridge Tour Page

def golden_gate_bridge(request):

    # Check if form is submitted
    if request.method == 'POST':

        # Get the form data
        submitted_tour_form = request.POST

        # Extract data from the submitted Form
        name = submitted_tour_form['name']
        email = submitted_tour_form['email']
        date = submitted_tour_form['tour_date']
        number_of_people = submitted_tour_form['number_of_people']

        # Create a Tour Reservation
        new_tour = Tour.objects.create(name=name, email=email, tour_date=date,number_of_people=number_of_people)

        # redirect the thank-you page after users created a new tour
        return redirect("/thank-you/")





    tour_form = TourForm()

    context = {
        'tour_form' : tour_form,
    }


    return render(request,'landing_pages/golden_gate_bridge.html', context)


# Contact Page

def contact(request):
    return render(request, 'landing_pages/contact.html')


def thank_you(request):
    return render(request, 'landing_pages/thank-you.html')