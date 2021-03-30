# Price Movements
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance
import datetime as dt
import math
import matplotlib.dates as mpl_dates

# Initiate Variable
levels = []
result = []


def process(stock):
    levels = []
    name = stock + '.JK'
    ticker = yfinance.Ticker(name)
    df = ticker.history(interval="1d", start="2020-03-03", end=dt.datetime.now())

    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)

    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]

    def isSupport(df, i):
        support = df['Low'][i] < df['Low'][i - 1] < df['Low'][i - 2] and df['Low'][i] < df['Low'][i + 1] < df['Low'][
            i + 2]
        return support

    def isResistance(df, i):
        resistance = df['High'][i] > df['High'][i - 1] > df['High'][i - 2] and df['High'][i] > df['High'][i + 1] > \
                     df['High'][i + 2]
        return resistance

    for i in range(2, df.shape[0] - 2):
        if isSupport(df, i):
            levels.append((i, df['Low'][i]))
        elif isResistance(df, i):
            levels.append((i, df['High'][i]))

    s = np.mean(df['High'] - df['Low'])

    def isFarFromLevel(l):
        return np.sum([abs(l - x) < s for x in levels]) == 0

    for i in range(2, df.shape[0] - 2):
        levels = []
        date_in = []
        if isSupport(df, i):
            l = df['Low'][i]
            d = "Low at " + str(datetime.strftime(df.index[i], '%d %b %Y'))

            if isFarFromLevel(l):
                temp = {
                    "price": math.floor(l),
                    "from": d
                }
                result.append(temp)
                levels.append((i, math.floor(l)))
                date_in.append((i, d))

        elif isResistance(df, i):
            l = df['High'][i]
            d = "High at " + str(datetime.strftime(df.index[i], '%d %b %Y'))

            if isFarFromLevel(l):
                levels.append((i, math.floor(l)))
                date_in.append((i, d))
                temp = {
                    "price": math.floor(l),
                    "from": d
                }
                result.append(temp)


def results(stock):
    del levels[:]
    del result[:]
    process(stock)
    return result
