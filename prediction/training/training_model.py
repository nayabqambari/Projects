import numpy as np 
import pandas as pd 
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers 
from tensorflow.keras import optimizers 
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dropout

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df = pd.read_csv('set_data.csv')


x = df[['Land area',  'No of rooms', 'No of Kitchens', 'No of Bathrooms', 'No of Stories', 
       'House Type', 'House nearby', 'Property type', 'Quality of gas', 'Supply of water', 
       'House towards', 'Parking Area', 'Crime Rate']]
y = df[['House Price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

x = np.array(x)
y = np.array(y)

x_train_n = np.array(x_train)
x_test_n = np.array(x_test)
y_train_n = np.array(y_train)
y_test_n = np.array(y_test)

x_train_n = ( x_train_n - x.mean(axis=0) ) / x.std(axis=0)
x_test_n = ( x_test_n - x.mean(axis=0) ) / x.std(axis=0)


def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(x_train_n.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(Dropout(0.1))
    model.add(layers.Dense(1))
    model.compile(optimizer=Adam(0.00001), loss='mse', metrics=['mae'])
    print(model.summary())
    return model


model = build_model()

r = model.fit(x_train_n, y_train_n, validation_data=(x_test_n,y_test_n), batch_size=1, epochs=500, verbose=1)


model.save("saved_models500")

model.save_weights("weights500.h5")