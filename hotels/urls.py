
from django.urls import path
from .views import index, detail,home


urlpatterns = [
    path('', home,name='home'),
    path('result', index , name='index'),
    path('<id>' , detail , name='detail')
    
]