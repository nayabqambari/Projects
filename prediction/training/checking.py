import numpy as np 
import pandas as pd 
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split


m = models.load_model('saved_models1000')
m.load_weights("weights1000.h5")

df = pd.read_csv('set_data.csv')


x = df[['Land area',  'No of rooms', 'No of Kitchens', 'No of Bathrooms', 'No of Stories', 
       'House Type', 'House nearby', 'Property type', 'Quality of gas', 'Supply of water', 
       'House towards', 'Parking Area', 'Crime Rate']] 


new_data = [2531, 7, 2, 7, 2, 4, 1, 3, 2, 7, 1, 11, 10]
# 32000000

new_data = ( new_data - x.mean(axis=0) ) / x.std(axis=0)

nd = new_data.values.reshape(1,-1)
ndd = nd.tolist()

p = m.predict(ndd)

print(p[0][0])
