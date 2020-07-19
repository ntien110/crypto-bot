import ccxt
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import finplot as fplt

exchange = ccxt.binance()
symbol = "BTC/USDT"
timeframe = "1d"
since = int(time.time()) - 356 * 24 * 60 * 60

exchange.load_markets()
data = exchange.fetch_ohlcv(symbol, timeframe, since*1000)

# Save to file
# header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
# df = pd.DataFrame(data, columns=header).set_index('Timestamp')
# symbol_out = symbol.replace("/","-")
# filename = '{}-{}-{}.csv'.format(exchange, symbol_out,timeframe)
# df.to_csv(filename)

# -------------------------------line graph-----------------------------------------------------
# def extractData(arr):
#     result = [[] for i in range(len(arr[0]))]
#     for ele in arr:
#         for i in range(len(ele)):
#             result[i].append(ele[i])
#     return result
# timestamp, openVal, high, low, closeVal, volume= extractData(data)
#
# fig, ax1 = plt.subplots()
#
# ax1.set_xlabel('timestamp (s)')
# ax1.set_ylabel('USDT')
# ln1 = ax1.plot(timestamp, openVal, color="green", linewidth=0.6, alpha=0.7, label="open")
# ln2 = ax1.plot(timestamp, high, color="purple", linewidth=0.6, alpha=0.7, label="high")
# ln3 = ax1.plot(timestamp, low, color="gray", linewidth=0.6, alpha=0.7, label="low")
# ln4 = ax1.plot(timestamp, closeVal, color="red", linewidth=0.6, alpha=0.7, label="close")
# #ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
# ax2.set_ylabel('volume', color='blue')  # we already handled the x-label with ax1
# ln5 = ax2.plot(timestamp, volume, color='blue', linewidth=0.6, alpha=0.7, label="volume")
# ax2.tick_params(axis='y', labelcolor='blue')
#
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
#
# lns = ln1+ln2+ln3 + ln4 + ln5
# labs = [l.get_label() for l in lns]
# ax1.legend(lns, labs, loc=0)
#
# plt.show()
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------candlestick chart-------------------------------------------------------

# format it in pandas
header = ['time', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(data, columns= header)
df = df.astype({'time':'datetime64[ns]'})

# create two plots
ax = fplt.create_plot(symbol, rows=1)

# plot candle sticks
candles = df[['time','open','close','high','low']]
fplt.candlestick_ochl(candles, ax=ax)

# overlay volume on the top plot
volumes = df[['time','open','close','volume']]
fplt.volume_ocv(volumes, ax=ax.overlay())

# restore view (X-position and zoom) if we ever run this example again
fplt.autoviewrestore()

# we're done
fplt.show()
