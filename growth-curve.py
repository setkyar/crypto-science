# https://www.lookintobitcoin.com/charts/200-week-moving-average-heatmap/
# Bitcoin Logarithmic Growth Curves

from datetime import date
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web

start = dt.datetime(2012, 1, 1)
end = dt.datetime.now()

# Get Bitcoin data from yahoo finance
df = web.DataReader('BTC-USD', 'yahoo', start, end)
df = df.reset_index()
df['date'] = pd.to_datetime(df['Date'])

## regression fitting
def funct(x, p1, p2):
	return p1*np.log(x) + p2

xdata = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['Close'])

popt, povc = curve_fit(funct, xdata, ydata, p0=(3.0,-10))

fittedydata = funct(xdata, popt[0], popt[1])

plt.style.use("dark_background")


plt.semilogy(df['date'], df['Close'])

for i in range(-3, 5):
	plt.plot(df['date'], np.exp(fittedydata + i))
	plt.fill_between(df['date'], np.exp(fittedydata + i - 1), np.exp(fittedydata + i), alpha = 0.4)

plt.ylim(bottom=1)

plt.show()