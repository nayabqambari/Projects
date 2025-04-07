from django.urls import re_path 
from . import views 
urlpatterns = [
    re_path(r'^api/data/$', views.single_prediction_api, name='api-data'),
    re_path('', views.prediction, name='prediction')
]