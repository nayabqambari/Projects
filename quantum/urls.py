
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls'), name="main"),  
    path('prediction/', include('prediction.urls'), name="prediction"), 
    path('contact_us/', include('contact_us.urls'), name="contact_us"),
    path('admin/', admin.site.urls),
]