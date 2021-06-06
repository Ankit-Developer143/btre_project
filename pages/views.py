from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def index(request):
    listings = Listing.objects.all()
    context = {
       'listings':listings,
       'state_choices': state_choices,
       'bedroom_choices': bedroom_choices,
       'price_choices': price_choices
   }

    return render(request,'pages/index.html',context)


def about(request):
    realtor = Realtor.objects.all();
    context  = {
        'realtors':realtor,
        
    }
    return render(request,'pages/about.html',context)