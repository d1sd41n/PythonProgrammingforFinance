import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=1)

#ten days split data
df_ohlc = df['Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#resets the index of the df, now the dates is not the index
df_ohlc.reset_index(inplace=True)

#convers the dates format datetime to  Matplotlib dates.
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#plotting with pure matplotlib
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()
