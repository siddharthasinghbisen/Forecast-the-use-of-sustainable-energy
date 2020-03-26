
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import array as arr


class dataanalyse:
    def trend(data):
        plt.figure(figsize=(8, 6))
        plt.plot(data['Year'], data['Coal (terawatt-hours)'], 'b-', label='Coal')
        plt.plot(data['Year'], data['Solar (terawatt-hours)'], 'r-', label='Solar')
        plt.plot(data['Year'], data['Crude oil (terawatt-hours)'], 'g-', label='Crude oil')
        plt.plot(data['Year'], data['Natural gas (terawatt-hours)'], 'm-', label='Natural gas')
        plt.plot(data['Year'], data['Traditional biofuels (terawatt-hours)'], 'c-', label='biofuels')
        plt.plot(data['Year'], data['Other renewables (terawatt-hours)'], 'y-', label='other')
        plt.plot(data['Year'], data['Hydropower (terawatt-hours)'], 'k-', label='Hydropower')
        plt.plot(data['Year'], data['Nuclear (terawatt-hours)'], color='#53049D', label='Nuclear')
        plt.plot(data['Year'], data['Wind (terawatt-hours)'], color='#9D0450', label='Wind')
        plt.plot(data['Year'], data['fossil_Fuels'], color='#474428', label='fossil_Fuels')
        plt.plot(data['Year'], data['Sustainable_Energy'], color='#858F00', label='Sustainable_Energy')
        plt.xlabel('Date in Year')
        plt.ylabel('Energy consumed by energy sources in terawatt-hours')
        plt.title('Energy consumption for every 10 year')
        plt.legend()
        return plt
        pass

    def pie(data):
        ar = []
        # To get the total sum of all columns
        for i in data.loc[:, data.columns != 'Year']:
            ar.append(data[i].sum())

        # To plot pie chart
        plt.figure(figsize=(8, 6))
        labels = "Coal (terawatt-hours)", "Solar (terawatt-hours)", "Crude oil (terawatt-hours)", "Natural gas (terawatt-hours)", "Traditional biofuels (terawatt-hours)", "Other renewables (terawatt-hours)", "Hydropower (terawatt-hours)", "Nuclear (terawatt-hours)", "Wind (terawatt-hours)", "fossil_Fuels", "Sustainable_Energy",
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'black', '#53049D', "#9D0450", "#858F00", "#474428", "red", "green"]
        explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.1)
        plt.pie(ar, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        return plt

        pass
