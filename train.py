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

from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


class training:
    def train(data):
        X = data.iloc[:, 2:10]
        y = data.iloc[:, 10:12]
        scaler = MinMaxScaler(feature_range=(0, 1))
        X_scaler = scaler.fit_transform(X)
        print(X_scaler)
        X_train, X_test, y_train, y_test = train_test_split(X_scaler, y, test_size=0.2, random_state=42, shuffle=False)
        X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
        X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

        model = Sequential()
        model.add(LSTM(30, input_shape=(1, 8,), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(15))
        model.add(Dropout(0.2))
        model.add(Dense(2, activation='relu'))

        model.compile(loss='mse', optimizer='adam')
        model.fit(X_train, y_train, epochs=200, batch_size=30, validation_split=0.2, verbose=2)
        Predictions = model.predict(X_test)

        lol = pd.DataFrame(Predictions)
        lol = lol.rename(columns={0: 'fossil_Fuels', 1: 'Sustainable_Energys'})
        print(lol)
        print(data['fossil_Fuels'])
        print
        plt.figure(figsize=(8, 6))
        test = data.iloc[:57, 10:11]
        p = np.append(test, lol.iloc[:, 1:2])
        plt.plot(p, label='prediction')
        plt.plot(data['fossil_Fuels'], label='actual')

        #plt.xlabel('Full data')
        #plt.ylabel('Energy consumed by energy sources in terawatt-hours')

        #plt.title('Energy consumption for every 10 year')
        plt.legend()
        plt.show()
