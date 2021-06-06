from django.http import request
from django.shortcuts import get_object_or_404, render
#import models Listing
from .models import Listing
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

#import Choices
from .choices import bedroom_choices,price_choices,state_choices

@login_required(login_url="/login/")
def index(request):
   listings = Listing.objects.all()
   
   context = {
       'listings':listings
   }
    
   return render(request,'listings/listings.html',context)
   
@login_required(login_url="/login/") 
def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk = listing_id)
    context = {
        'listing':listing,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'values': request.GET
    }
    return render(request,'listings/listing.html',context)
@login_required(login_url="/login/")  
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            
            
    #BedRooms (lte) exact or equal to
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
            
            
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {
        'listings':queryset_list
    }

    
    return render(request,'listings/search.html',context)