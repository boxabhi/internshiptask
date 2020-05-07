from django.shortcuts import render, get_object_or_404
from .models import Hotels, City, VendorType
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.


def home(request):
    venues = VendorType.objects.all()
    cities = City.objects.all()
    context = {
        'venues': venues,
         'cities' : cities
    }
    return render(request,'index.html', context)

def index(request):
    city = request.GET.get('city', '')
    vegprice = request.GET.get('vegprice',None)
    nonvegprice = request.GET.get('nonvegprice',None)
    venue = request.GET.get('venue' ,None)
    capacity = request.GET.get('capacity',None)
    
    hotels = Hotels()
    results = hotels.all_hotels(city,vegprice,nonvegprice,venue,capacity)
    return JsonResponse(results)


def cities(request):
    cities = City()
    result = cities.serialize()
    return JsonResponse(result)

def venues(request):
    venues = VendorType()
    result = venues.serialize()
    return JsonResponse(result)


def detail(request, id):
    try:
        hotel = Hotels.objects.get(id=id)
        hotel = (hotel.seralize_hotel())
    except Hotels.DoesNotExist:
        hotel = None
    return JsonResponse(hotel)

