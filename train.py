import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from split import splitit
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


class training:
    def train(data):

        n_steps_in = 8
        n_steps_out = 8
        X, y = splitit.split_sequences(data[:50].values, n_steps_in, n_steps_out)
        n_features = X.shape[2]
        # define model
        model = Sequential()
        model.add(LSTM(30, activation='relu', input_shape=(n_steps_in, n_features)))
        model.add(RepeatVector(n_steps_out))
        model.add(LSTM(20, activation='relu', return_sequences=True))
        model.add(TimeDistributed(Dense(1)))
        # model.compile(optimizer='adam', loss='mse', metrics=['mse',rmse,'mae',mape,merr])
        model.compile(optimizer='adam', loss='mse', metrics=['mse', 'mae', 'acc'])

        es = EarlyStopping(monitor='mae', mode='min', verbose=1, patience=100)
        mc = ModelCheckpoint('best_model2.h5', monitor='mae', mode='min', verbose=0, save_best_only=True)
        X1, y1 = splitit.split_sequences(data[50:70].values, n_steps_in, n_steps_out)
        history = model.fit(X, y, epochs=1500, verbose=2, validation_data=(X1, y1), callbacks=[es, mc])
        testx, testy = splitit.split_sequences(data[55:].values, n_steps_in, n_steps_out)
        yhat = model.predict(testx)
        yhat = yhat.reshape(8, 1)
        testy = testy.reshape(8, 1)
        yhat = pd.DataFrame(yhat).rename(columns={0: 'Predicted'})
        testy = pd.DataFrame(testy).rename(columns={0: 'Test'})

        predictions = pd.concat([yhat, testy], axis=1)
        predictions.plot()
