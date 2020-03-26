from analyse import dataanalyse
from preprocess import preprocess
import pandas as pd


# load data
# analyze
# preprocess


def main():
    energy = preprocess.getdata()
    # to plot trend graph
    trend = dataanalyse.trend(energy)
    trend.show()
    # to plot pie chart
    # dataanalyse.pie(energy)
    pie = dataanalyse.pie(energy)
    pie.show()
    heatmap = dataanalyse.heatmap1(energy)
    heatmap.show()
    print(energy)


if __name__ == '__main__':
    main()
