from analyse import dataanalyse
from preprocess import preprocess
from train import training
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask


''' main function 

	energy = to preprocess the data by adding columns or removing unwanted data points
	
	trend = A variable to analyse the trend of data for each year
	
	pie = to plot pie chart
'''


def main():
    energy = preprocess.getdata()

    trend = dataanalyse.trend(energy)

    pie = dataanalyse.pie(energy)
    # to plot heatmap
    heatmap = dataanalyse.heatmap1(energy)
    # normalizeddata = preprocess.getnormdata(energy)
    model = training.train(energy)
#------------------------------------------------------------------

    ''' Flask HTML page for the Web application
		
		app = an instance for creating the web application
		
		home = Function that will be called when user is on default page("/")
		
		Having debug=True allows possible Python errors to appear on the web page'''


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == '__main__':
    main()
    app.run(debug=True)
