# https://www.lookintobitcoin.com/charts/200-week-moving-average-heatmap/
# 200 Week Moving Average Heatmap
#

from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web

start = dt.datetime(2012, 1, 1)
end = dt.datetime.now()

# Get Bitcoin data from yahoo finance
df = web.DataReader('BTC-USD', 'yahoo', start, end)
df = df.reset_index()

df['200wma'] = df['Close'].rolling(window = 1400).mean()
df = df[1400:]
dates = pd.to_datetime(df['Date'])

# slice every thirty days
monthly = df[::30]

distance = monthly['200wma'].pct_change() * 100

plt.style.use("dark_background")

plt.semilogy(dates, df['Close'], color = "grey", zorder = 1)
plt.semilogy(dates, df['200wma'], color = "purple", zorder = 2)

plt.scatter(monthly['Date'], monthly['Close'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 3 )

cbar = plt.colorbar()
cbar.set_label("% monthly increase in 200wma")
cbar.ax.yaxis.set_label_position("left")

plt.show()