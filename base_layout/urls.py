from django.urls import path
from . import views
urlpatterns = [
    path('', views.base_layout, name='base_layout'),
]