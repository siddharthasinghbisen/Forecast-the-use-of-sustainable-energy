from analyse import dataanalyse
from preprocess import preprocess
from train import training
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask


''' 
	app = an instance for creating the web application

	main function 

	energy = to preprocess the data by adding columns or removing unwanted data points
	
	trend = A variable to analyse the trend of data for each year
	
	pie = to plot pie chart
'''

app = Flask(__name__)


def main():
    energy = preprocess.getdata()

    trend = dataanalyse.trend(energy)
    trend.savefig('D:/exam/ML/Energy consumption/images/Trend.png')
    pie = dataanalyse.pie(energy)
    pie.savefig('D:/exam/ML/Energy consumption/images/pie.png')

    # to plot heatmap
    heatmap = dataanalyse.heatmap1(energy)
    heatmap.savefig('D:/exam/ML/Energy consumption/images/heatmap.png')

    # normalizeddata = preprocess.getnormdata(energy)
    model = training.train(energy)
    model.savefig('D:/exam/ML/Energy consumption/images/predictions.png')
#------------------------------------------------------------------

    ''' Flask HTML page for the Web application
		
		
		home = Function that will be called when user is on default page("/")
		
		Having debug=True allows possible Python errors to appear on the web page'''


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/prediction")
def prediction():
    return "Hello, Predictions"


if __name__ == '__main__':
    app.run(debug=True)
    main()
