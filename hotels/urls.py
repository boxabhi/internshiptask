
from django.urls import path
from .views import index, detail,home
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home,name='home'),
    path('result', index , name='index'),
    path('detail/<id>' , detail , name='detail'),
   
    
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()