from django.shortcuts import render, get_object_or_404
from .models import Hotels, City, VendorType
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request,'index.html')

def index(request):
    results = {}
    city = request.GET.get('city', '')
    vegprice = request.GET.get('vegprice',None)
    nonvegprice = request.GET.get('nonvegprice',None)
    venue = request.GET.get('venue' ,None)
    capacity = request.GET.get('capacity',None)
    
    hotels = Hotels()
    results = hotels.all_hotels(city,vegprice,nonvegprice,venue,capacity)
    return JsonResponse(results)
    
    # if request.method == 'GET':
    #     city = request.GET.get('city')
    #     if city is not None:
    #         hotels = Hotels.objects.filter(city=city).all()
    #     else:
    #         hotels = Hotels.objects.all()
    #     paginator = Paginator(hotels , 9)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     print(city)
    # else:
    #     hotels = Hotels.objects.all()
    #     paginator = Paginator(hotels , 9)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
        
    # cities = City.objects.all()
    # venues = VendorType.objects.all()
    # context = {
    #     'cities': cities,
    #     'venues': venues,
    #     'page_obj': page_obj
    # }
    
    # return render(request, 'index.html' ,context)


def detail(request, id):
    try:
        hotel = Hotels.objects.get(id=id)
        hotel = (hotel.seralize_hotel())
    except Hotels.DoesNotExist:
        hotel = None
    return JsonResponse(hotel)

