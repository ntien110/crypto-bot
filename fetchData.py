import ccxt
import pandas as pd

def fetchMarketData(_exchange, _symbol, _timeframe='1d', _since=0, _limit=1000, _params={}):
    try:
        exchange = getattr(ccxt, _exchange)()
    except AttributeError:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('Exchange "{}" not found. Please check the exchange is supported.'.format(_exchange))
        print('-' * 80)
        return None

    # Check if fetching of OHLC Data is supported
    if exchange.has["fetchOHLCV"] != True:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('{} does not support fetching OHLC data. Please use another exchange'.format(_exchange))
        print('-' * 80)
        return None

    # Check requested timeframe is available. If not return a helpful error.
    if (not hasattr(exchange, 'timeframes')) or (_timeframe not in exchange.timeframes):
        print('-' * 36, ' ERROR ', '-' * 35)
        print('The requested timeframe ({}) is not available from {}\n'.format(_timeframe, _exchange))
        print('Available timeframes are:')
        for key in exchange.timeframes.keys():
            print('  - ' + key)
        print('-' * 80)
        return None

    # Check if the symbol is available on the Exchange
    exchange.load_markets()
    if _symbol not in exchange.symbols:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('The requested symbol ({}) is not available from {}\n'.format(_symbol, _exchange))
        print('Available symbols are:')
        for key in exchange.symbols:
            print('  - ' + key)
        print('-' * 80)
        return None

    return exchange.fetch_ohlcv(symbol=_symbol, timeframe=_timeframe, since=_since, limit=_limit, params=_params)

def fetchMarketDataToFile(_exchange, _symbol, _timeframe='1d', _since=0, _limit=1000, _params={}, _fileName=None):
    data = fetchMarketData(_exchange, _symbol, _timeframe, _since, _limit, _params)
    if data is None:
        return None
    header = ['timestamp', 'openVal', 'high', 'low', 'closeVal', 'volume']
    df = pd.DataFrame(data, columns=header).set_index('timestamp')
    if _fileName is None or not isinstance(_fileName, str):
        symbol_out = _symbol.replace("/","-")
        _filename = '{}-{}-{}.csv'.format(_exchange, symbol_out,_timeframe)
    df.to_csv(_filename)
    return _fileName
