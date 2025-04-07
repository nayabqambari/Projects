from django.urls import path
from . import views
urlpatterns = [
    path('contact_post', views.contact_post, name='contact_post'),
    path('', views.contact_us, name='contact_us'),
]