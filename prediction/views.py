#####################################       general imports      ##########################################
from django.shortcuts import render
from django.http import JsonResponse 

#####################################       deep learning imports       ##########################################
import numpy as np 
import pandas as pd 
from tensorflow.keras import models  
from .form import InputForm  



####################################    company prediction      ###########################################
def prediction(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        return render(request, 'prediction.html', {'form':form})
    else:
        form = InputForm()
        return render(request, 'prediction.html', {'form':form})


#######################################     model     ###################################################
def myModel(crime_rate, parking_area, house_near_by, house_towards, house_type, stories, supply_of_water, address, rooms, bathrooms, kitchens, land_area, property_type, quality_of_gas):
    
    file = 'prediction/training/' + 'set_data.csv' 
    df = pd.read_csv(file)

    x = df[['Land area',  'No of rooms', 'No of Kitchens', 'No of Bathrooms', 'No of Stories', 
       'House Type', 'House nearby', 'Property type', 'Quality of gas', 'Supply of water', 
       'House towards', 'Parking Area', 'Crime Rate']]

    new_data = [int(land_area), int(rooms), int(kitchens), int(bathrooms), int(stories), int(house_type), int(house_near_by), int(property_type), int(quality_of_gas), int(supply_of_water), int(house_towards), int(parking_area), int(crime_rate)]

    # ||    #############     standardization of data      ####################    ||
    new_data = ( new_data - x.mean(axis=0) ) / x.std(axis=0)
    nd = new_data.values.reshape(1,-1)
    ndd = nd.tolist()

    # ||    #############     load the model      ####################    || 

    m = models.load_model('prediction/saved_models23/')
    m.load_weights("prediction/weights23.h5")

    pre_values = m.predict(ndd)

    return pre_values


#######################################     api     ################################################
def single_prediction_api(request): 
    address = request.GET['address']
    land_area = request.GET['land_area']
    rooms = request.GET['rooms']
    bathrooms = request.GET['bathrooms']
    kitchens = request.GET['kitchens']
    stories = request.GET['stories']
    house_type = request.GET['house_type']
    property_type = request.GET['property_type']
    house_near_by = request.GET['house_near_by']
    house_towards = request.GET['house_towards']
    quality_of_gas = request.GET['quality_of_gas']
    supply_of_water = request.GET['supply_of_water']
    parking_area = request.GET['parking_area']
    crime_rate = request.GET['crime_rate']

    predicted_data = myModel(crime_rate, parking_area, house_near_by, house_towards, house_type, stories, supply_of_water, address, rooms, bathrooms, kitchens, land_area, property_type, quality_of_gas)              ## ==> myModel()
   
    data = { 
        'pre_data' : predicted_data.tolist()[0][0],
        }
    return JsonResponse(data)
