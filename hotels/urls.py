
from django.urls import path
from .views import index, detail,home,cities,venues


urlpatterns = [
    path('', home,name='home'),
    path('result', index , name='index'),
    path('cities', cities , name='cities'),
    path('venues' , venues ,name='venues'),
    path('<id>' , detail , name='detail'),
   
    
]