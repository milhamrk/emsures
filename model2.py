# Moving Average
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
import mplfinance as mpf

start = '2010-02-19'
end = dt.datetime.now()

stock = 'BBCA.JK'
df = yf.download(stock, start, end, interval='1d')

ma20 = 20
ma50 = 50
ma100 = 100
ma200 = 200
SMAs = [ma20, ma50, ma100, ma200]

for i in SMAs:
    df["MA" + str(i) + " Daily"] = round(df.iloc[:, 4].rolling(window=i).mean())

print(df.tail(1))