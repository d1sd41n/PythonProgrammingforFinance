
import numpy as np
import pandas as pd
import pickle
from collections import Counter

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv')
    tickers = df.columns.values.tolist() # get the values of the colums on list
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    #print(df.columns.values.tolist())
    return tickers, df
