# Moving Average
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
import mplfinance as mpf

start = '2020-02-19'
end = dt.datetime.now()

stock = 'AALI.JK'
df = yf.download(stock, start, end, interval='1d')

short_sma = 20
long_sma = 50
SMAs = [short_sma, long_sma]

for i in SMAs:
    df["SMA_" + str(i)] = round(df.iloc[:, 4].rolling(window=i).mean())

print(df.tail(3))

# CANDLE VERSION
# plt.rcParams['figure.figsize'] = [15, 7]
#
# plt.rc('font', size=14)

# df['Date'] = pd.to_datetime(df.index)
# df['Date'] = df['Date'].apply(mpl_dates.date2num)
#
# df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close', 'SMA_20', 'SMA_50']]


# def plot_all():
#     fig, ax = plt.subplots()
#
#     candlestick_ohlc(ax, df.values, width=0.6,
#                      colorup='green', colordown='red', alpha=0.8)
#
#     date_format = mpl_dates.DateFormatter('%d %b %Y')
#     ax.xaxis.set_major_formatter(date_format)
#     fig.autofmt_xdate()
#
#     fig.tight_layout()
#
#     fig.show()
#
#
# plot_all()
# END OF CANDLE VERSION

mpf.plot(df, type = 'ohlc',figratio=(16,6),
         mav=(short_sma,long_sma),
         title= str(stock),
         style='default')
