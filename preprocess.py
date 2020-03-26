import pandas as pd


class preprocess:
    def getdata():
        # Read CSV file
        data = pd.read_csv("WorldEnergyConsuptions1.csv")
        # Add a column to show increase in usage of fossil fuel around the globe since 1800
        data['fossil_Fuels'] = data['Coal (terawatt-hours)'] + data['Crude oil (terawatt-hours)'] + data['Natural gas (terawatt-hours)']
        #  Add a column to show increase in usage of sustainable energy source around the globe since 1800
        data['Sustainable_Energy'] = data['Solar (terawatt-hours)'] + data['Traditional biofuels (terawatt-hours)'] + data['Other renewables (terawatt-hours)'] + data['Hydropower (terawatt-hours)'] + data['Nuclear (terawatt-hours)'] + data['Wind (terawatt-hours)']

        return data
