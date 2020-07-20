import fetchData
import visualizeData
import time

# config
exchange = 'binance'
symbol = "BTC/USDT"
timeframe = "1d"
since = (int(time.time()) - 356 * 24 * 60 * 60) * 1000
limit = 1000
# ---------------------------------------------------------------------------------------------------------

data = fetchData.fetchMarketData(exchange, symbol, timeframe, since, limit)
if data is None:
    quit()
timestamp, openVal, high, low, closeVal, volume = visualizeData.extractDataFromList(data)

#---------------------------------------- line gragh-----------------------------------------------------------
# visualizeData.drawOhlcvLineGragh(timestamp, openVal, high, low, closeVal, volume, symbol.split('/')[1])
#--------------------------------------------------------------------------------------------------------------

# --------------------------------------candlestick chart-------------------------------------------------------
# visualizeData.drawCandleStickChart(timestamp, openVal, high, low, closeVal, volume, exchange, symbol)
#---------------------------------------------------------------------------------------------------------------
