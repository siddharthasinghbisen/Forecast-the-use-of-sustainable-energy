from analyse import dataanalyse
#from preprocess import preprocess
import pandas as pd

# load data
# analyze
# preprocess


def main():
    # Read CSV file
    data = pd.read_csv("WorldEnergyConsuptions1.csv")
    # Add a column to show increase in usage of fossil fuel around the globe since 1800
    data['fossil_Fuels'] = data['Coal (terawatt-hours)'] + data['Crude oil (terawatt-hours)'] + data['Natural gas (terawatt-hours)']
    #  Add a column to show increase in usage of sustainable energy source around the globe since 1800
    data['Sustainable_Energy'] = data['Solar (terawatt-hours)'] + data['Traditional biofuels (terawatt-hours)'] + data['Other renewables (terawatt-hours)'] + data['Hydropower (terawatt-hours)'] + data['Nuclear (terawatt-hours)'] + data['Wind (terawatt-hours)']

    print(data)
    # to plot trend graph
    analyze = dataanalyse.trend(data)
    # to plot pie chart
    print(dataanalyse.pie(data))


if __name__ == '__main__':
    main()
