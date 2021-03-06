# Moving Average
import pandas as pd
import yfinance as yf
from datetime import datetime as dt, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
import mplfinance as mpf

start = '2010-02-19'
end = dt.now()

stock = 'BBCA.JK'
# df = yf.download(stock, start, end, interval='1d').dropna()
ticker = yf.Ticker(stock)
df = ticker.history(interval="1d", start=dt.now() - timedelta(days=365), end=dt.now())
df = df.dropna()
ma20 = 20
ma50 = 50
ma100 = 100
ma200 = 200
SMAs = [ma20, ma50, ma100, ma200]

for i in SMAs:
    df["MA" + str(i) + " Daily"] = round(df['Close'].rolling(window=i).mean())

df = df.loc[:, ['MA20 Daily', 'MA50 Daily', 'MA100 Daily', 'MA200 Daily']]
print(df.tail(1)['MA20 Daily'][0])