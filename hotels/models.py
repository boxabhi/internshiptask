from django.db import models
from django_mysql.models import ListCharField
# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def find_city(city):
        city = City.objects.filter(city = city).first()
        return city.city
    
    def serialize(self):
        cities = City.objects.all()
        print(cities)
        result = []
        for city in cities:
            result.append(city.city)
        response = {}
        response['cities'] = result
        
        return response
            
    
    def __str__(self):
        return self.city

class VendorType(models.Model):
    vendor_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vendor_type
    
    class Meta:
        ordering = ['vendor_type']
        
   # Serialization for Vendortype     
    def serialize(self):
        venues = VendorType.objects.all()
        result = []
        for venue in venues:
            result.append(venue.vendor_type)
        response = {}
        response['venues'] = result
        
        return response
        
        
class Hotels(models.Model):
    vendor_name = models.CharField(max_length=500 , blank=False)
    veg_price = models.FloatField()
    non_veg_price = models.FloatField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    maximum = ListCharField(base_field = models.IntegerField() , max_length=10)
    minimum = ListCharField(base_field = models.IntegerField() , max_length=10)
    vendor_type = models.ManyToManyField(VendorType)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    highlights = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.vendor_name
    
    
    def serialize(self,vendor_types):
        result = []
        for vendor in vendor_types:
            result.append(vendor.vendor_type)
        return result
    
    def is_valid_queryparam(param):
        return param != '' and param is not None
    

    # Method for searching and seralizeHotel
    def all_hotels(self, city , vegprice , nonvegprice , venue , capacity):
        results = {}
       
        hotels = Hotels.objects.all()
        
        if city:
            hotels = hotels.filter(city = City.objects.filter(city=city).first())
            
        if vegprice: 
            hotels = hotels.filter(veg_price__range=(0 , vegprice))
        
        if nonvegprice:
            hotels = hotels.filter(non_veg_price__range=(0 , nonvegprice))
        
        if venue:
            hotels = hotels.filter(vendor_type__vendor_type = venue)
                
        if capacity:
            hotels = hotels.filter(maximum__1__level__gte = capacity)
            
            
        
        for index in range(0, len(hotels)):
            results[index] = hotels[index].seralize_hotel()
        return results
            
    
    def seralize_hotel(self):
        return {
            'id' : self.id,
            'hotel' : self.vendor_name,
            'veg_price' : self.veg_price,
            'non_veg_price' : self.non_veg_price,
            'city' :  City.find_city(self.city),
            'maximum' : {
                'start' : self.maximum[0],
                 'end' : self.maximum[1],
            },
            'minimum': {
                'start' : self.minimum[0],
                'end'   : self.minimum[1]
            },
            'vendor_type' : self.serialize(list(self.vendor_type.all())) ,
            'phone' : self.phone,
            'highlights' : self.highlights,
            'about' : self.about,
            'address' : self.address,
            
        }
        
        
              
        
        


        
            
