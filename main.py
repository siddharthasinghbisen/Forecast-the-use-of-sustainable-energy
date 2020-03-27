from analyse import dataanalyse
from preprocess import preprocess
import pandas as pd
import matplotlib.pyplot as plt


# load data
# analyze
# preprocess


def main():
    energy = preprocess.getdata()
    # to plot trend graph
    trend = dataanalyse.trend(energy)
    # to plot pie chart
    pie = dataanalyse.pie(energy)
    # to plot heatmap
    heatmap = dataanalyse.heatmap1(energy)

    normalizeddata = preprocess.getnormdata(energy)


if __name__ == '__main__':
    main()
