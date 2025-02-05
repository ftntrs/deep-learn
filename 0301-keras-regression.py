import pandas as pd
import numpy as np
import keras
import os

import warnings
warnings.simplefilter('ignore', FutureWarning)

url='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv'
file='concrete_data.csv'

# os.system('wget ' + url)

concrete_data = pd.read_csv(file)
print(concrete_data.head())
print(concrete_data.shape)

concrete_data.describe()
concrete_data.isnull().sum()

concrete_data_columns = concrete_data.columns
predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column

print(predictors.head())
print(target.head())

predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()

n_cols = predictors_norm.shape[1] # number of predictors

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Input

# define regression model
# The above function create a model that has two hidden layers, each of 50 hidden units.
def regression_model():
    # create model
    model = Sequential()
    model.add(Input(shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# build the model
model = regression_model()

# fit the model
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)















