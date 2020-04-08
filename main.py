from analyse import dataanalyse
from preprocess import preprocess
from train import training
import pandas as pd
import matplotlib.pyplot as plt


def main():
    energy = preprocess.getdata()
    # to plot trend graph
    trend = dataanalyse.trend(energy)
    # to plot pie chart
    pie = dataanalyse.pie(energy)
    # to plot heatmap
    heatmap = dataanalyse.heatmap1(energy)
    #normalizeddata = preprocess.getnormdata(energy)
    model = training.train(energy)
    ''' Flask HTML page for the graphs'''


if __name__ == '__main__':
    main()
