import pandas as pd
from train import training
import sns


'''
    gerdata function is to get the data and preprocess it for training
   
    getnormdata function is to normalize the data in range of (0, 1) and reverese using getdenormdata function
   
    normalize function takes 3 parameters(values from the selected column, minn in the column and max from that column) 
    is set of mathematical calculations that converts the given value in scalar form and back to normal value using 
    function denormalize.

'''


class preprocess:
    def getdata():
        # Read CSV file
        data = pd.read_csv("WorldEnergyConsuptions1.csv")
        # Add a column to show increase in usage of fossil fuel around the globe since 1800
        data['fossil_Fuels'] = data['Coal (terawatt-hours)'] + data['Crude oil (terawatt-hours)'] + data['Natural gas (terawatt-hours)']
        #  Add a column to show increase in usage of sustainable energy source around the globe since 1800
        data['Sustainable_Energy'] = data['Solar (terawatt-hours)'] + data['Traditional biofuels (terawatt-hours)'] + data['Other renewables (terawatt-hours)'] + data['Hydropower (terawatt-hours)'] + data['Nuclear (terawatt-hours)'] + data['Wind (terawatt-hours)']
        return data

    # to  normalize the data other than year between o and 1
    def getnormdata(data):
        for i in data.loc[:, data.columns != 'Year']:
            data[i] = preprocess.normalize(data[i], data.values.max(), data.values.min())
        return data

    def getdenormdata(data):
        for i in data.loc[:, data.columns != 'Year']:
            data[i] = preprocess.denormalize(data[i], data.values.max(), data.values.min())
        return data

    # formula of normalization
    def normalize(value, minn, maxx):
        normalized = (value - minn) / (maxx - minn)
        return normalized

    # formula of denormalization
    def denormalize(normalized, minn, maxx):
        denormalized = (normalized * (maxx - minn) + minn)
        return denormalized
