import numpy as np 
import pandas as pd
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers 
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from datetime import timedelta, datetime
  
# t = 'ASL'
# t = 'BAFL'
# t = 'BAHL'
# t = 'BOP'
# t = 'DGKC'
# t = 'EFERT'
# t = 'ENGRO'
# t = 'FCCL'
# t = 'FFC'
# t = 'HASCOL'
# t = 'HBL'
# t = 'HUBC'
# t = 'HUMNL'
# t = 'ISL'
# t = 'LOTCHEM'
# t = 'MCB'
# t = 'MEBL'
# t = 'MLCF'
# t = 'NML'
# t = 'OGDC'
# t = 'PAEL'
# t = 'POL'
# t = 'PPL'
# t = 'PRL'
# t = 'PSO'
# t = 'PTC'
# t = 'SNGP'
# t = 'TRG'
# t = 'UBL'
# t = 'UNITY'
t = 'PIBTL'


company = t.lower() 
filename = str(company) + '.csv' 
all_data_filename = str(company) + '/' + filename
train_filename = str(company) + '/train_' + str(company) + '.csv' 
test_filename = str(company) + '/test_' + str(company) + '.csv'
model_path = 'saved_model/'+ str(company) 

dfff = pd.read_csv(all_data_filename) 
xxx = dfff[['open', 'low', 'high', 'close', 'volume']].values 
mean = xxx.mean(axis=0)
std = xxx.std(axis=0) 

df = pd.read_csv(train_filename)  
x = df[['open', 'low', 'high', 'close', 'volume']].values 
train_data = np.delete(x, (x.shape[0]-1), axis=0) 
train_targets = np.delete(x, 0, axis=0) 

dff = pd.read_csv(test_filename)  
y = dff[['open', 'low', 'high', 'close', 'volume']].values 
test_data = np.delete(y, (y.shape[0]-1), axis=0) 
test_targets = np.delete(y, 0, axis=0)

dates = dff['date'].values 
dates = np.delete(dates, 0, axis=0) 



# ||    #############     standardization of data      ####################    ||
# mean = x.mean(axis=0)
# std = x.std(axis=0)

# print(mean)
# print(std)

train_data -= mean
train_data /= std
test_data -= mean
test_data /= std

train_targets -= mean  
train_targets /= std 
test_targets -= mean
test_targets /= std 


# ||    #############     building model      ####################    ||
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(5))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    print(model.summary())
    return model

fig, axs = plt.subplots(2, 3)  
fig.suptitle('Comparision Between Actual and Predicted close value for ' + str(company))

j=0

# ||    #############     K fold validation      ####################    ||
k = [5,8,10]
for ik in k:
    num_val_samples = len(train_data) // ik
    # num_epochs = 100
    # num_epochs = 500
    # num_epochs = 1000
    all_scores = []
    all_mae_histories = []
    all_mae = []
    all_mse = [] 
    print("\n||    #############     Validation Using K Fold Method      ####################    ||\n")
    print('||   Number of Folds # '+ str(ik) + '    ||\n')
    print('||   Number of Epochs # '+ str(num_epochs) + '    ||\n')
    model = build_model()
    for i in range(ik):
        print('||   Processing Fold # '+ str(i+1) + '    ||\n')
        val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
        val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
        partial_train_data = np.concatenate([train_data[:i * num_val_samples],train_data[(i + 1) * num_val_samples:]],axis=0)
        partial_train_targets = np.concatenate([train_targets[:i * num_val_samples],train_targets[(i + 1) * num_val_samples:]],axis=0)
        # model = build_model()
        history = model.fit(partial_train_data, partial_train_targets,validation_data=(val_data, val_targets),epochs=num_epochs, batch_size=16, verbose=0)
        # model.save(model_path+"/final_model/") 
        mae_history = history.history['mae']
        all_mae_histories.append(mae_history)
        test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
        all_mae.append(test_mae_score)
        all_mse.append(test_mse_score)
    
    # print("mean absolute error: " + str(round(np.mean(all_mae), 2)))
    # print("mean square error: " + str(round(np.mean(all_mse), 2)))
    model.save(model_path+"/"+ str(ik) + "/" + str(num_epochs) +"/") 
    

    predict_targets = model.predict(test_data)
 
    testTargets = test_targets * std
    testTargets = testTargets + mean
    predict_targets *= std 
    predict_targets += mean
    dates = pd.to_datetime(dates) 
    
    axs[0, j].set_title('K=' + str(ik) + " epoch=" + str(num_epochs))
    axs[0, j].plot(dates, testTargets[:,3], label='Actual close')
    axs[0, j].plot(dates, predict_targets[:,3], label='Predicted close') 
    axs[0, j].set_xlabel('Date')
    axs[0, j].set_ylabel('Value') 
    # axs[0, j].tick_params(labelrotation=45)
    for tick in axs[0, j].get_xticklabels():
        tick.set_rotation(45)



    average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
    axs[1, j].plot(range(1, len(average_mae_history) + 1), average_mae_history, label="MAE")
    axs[1, j].set_title('MAE=' + str(round(np.mean(all_mae), 2)) + " MSE=" + str(round(np.mean(all_mse), 2)))
    axs[1, j].set_xlabel('Epochs')
    axs[1, j].set_ylabel('Validation MAE')
    axs[1, j].legend() 

    j +=1;

    # average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
    # plt.plot(range(1, len(average_mae_history) + 1), average_mae_history, label="MAE")
    # plt.xlabel('Epochs')
    # plt.ylabel('Validation MAE')
    # plt.title('Mean Absolute Error History')
    # plt.legend()
    # plt.show()


# plt.gcf().autofmt_xdate() 

plt.tight_layout() 
plt.show() 

# ||    #############     Testing the model      ####################    || 
# model = models.load_model(model_path+"/training")
# model = models.load_model(model_path+"/1")
# model = build_model()
# model.fit(train_data, train_targets,epochs=500, batch_size=32, verbose=1)
# test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
# print('||   Test MSE Score # '+ str(test_mse_score) + '    ||\n')
# print('||   Test MAE Score # '+ str(test_mae_score) + '    ||\n') 
# model.save(model_path+"/final_training")

#  #############     Model's Prediction on Test Data     ####################
# predict_targets = model.predict(test_data)
 
# test_targets *= std
# test_targets += mean
# predict_targets *= std 
# predict_targets += mean
# dates = pd.to_datetime(dates) 

# plt.figure(figsize=(12, 6))
# plt.plot(dates, test_targets[:,3], label='Actual close')
# plt.plot(dates, predict_targets[:,3], label='Predicted close')
# plt.title('Comparision Between Actual close and Model Predicted close')
# plt.legend()
# plt.show()


# plt.figure(figsize=(12, 6))
# plt.plot(dates, test_targets[:,0], label='Actual open')
# plt.plot(dates, predict_targets[:,0], label='Predicted open')
# plt.title('Comparision Between Actual open and Model Predicted open')
# plt.legend()
# plt.show()

 
# plt.figure(figsize=(12, 6))
# plt.plot(dates, test_targets[:,1], label='Actual low')
# plt.plot(dates, predict_targets[:,1], label='Predicted low')
# plt.title('Comparision Between Actual low and Model Predicted low')
# plt.legend()
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.plot(dates, test_targets[:,2], label='Actual high')
# plt.plot(dates, predict_targets[:,2], label='Predicted high')
# plt.title('Comparision Between Actual high and Model Predicted high')
# plt.legend()
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.plot(dates, test_targets[:,3], label='Actual close')
# plt.plot(dates, predict_targets[:,3], label='Predicted close')
# plt.title('Comparision Between Actual close and Model Predicted close')
# plt.legend()
# plt.show()