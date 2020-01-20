import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
# used for serialization
import pickle

# used for http request
import requests

import matplotlib.pyplot as plt
from matplotlib import style

import numpy as np

style.use('ggplot')


def visualize_data():
    df = pd.read_csv('nifty50_joined_closes.csv')
    ##    df['VEDL.NS'].plot()
    ##    plt.show()
    df_corr = df.corr()

    print(df_corr.head())
    df_corr.to_csv('niftyheatmap.csv')

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()


visualize_data()
