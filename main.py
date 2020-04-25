from analyse import dataanalyse
from preprocess import preprocess
from train import training
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask
from flask import Flask, render_template, url_for, request


'''
	app = an instance for creating the web application

	main function

	energy = to preprocess the data by adding columns or removing unwanted data points

	trend = A variable to analyse the trend of data for each year

	pie = to plot pie chart

	Flask HTML page for the Web application


	home = Function that will be called when user is on default page("/")

	Having debug=True allows possible Python errors to appear on the web page
'''

app = Flask(__name__)

# Home page


@app.route("/")
def home():
    energy = preprocess.getdata()
    trend = dataanalyse.trend(energy)
    trend.savefig('D:/exam/ML/Energy consumption/static/images/energytrends.png')

    trend2 = dataanalyse.trend2(energy)
    trend2.savefig('D:/exam/ML/Energy consumption/static/images/Trend2.png')
    pie = dataanalyse.pie(energy)
    pie.savefig('D:/exam/ML/Energy consumption/static/images/pie.png')

    # to plot heatmap
    heatmap = dataanalyse.heatmap1(energy)
    heatmap.savefig('D:/exam/ML/Energy consumption/static/images/heatmap.png')

    return render_template('home.html')


# Predictions Page
@app.route('/prediction', methods=['POST'])
def prediction():
    energy = preprocess.getdata()
    # normalizeddata = preprocess.getnormdata(energy)
    # train model and get predictions
    model = training.train(energy)
    model.savefig('D:/exam/ML/Energy consumption/static/images/predictions.png')
    return render_template('prediction.html')

#------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=False, threaded=False, host='0.0.0.0')
