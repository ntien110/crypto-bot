import matplotlib.pyplot as plt
import finplot as fplt

def extractDataFromList(arr):
    result = [[] for i in range(len(arr[0]))]
    for ele in arr:
        for i in range(len(ele)):
            result[i].append(ele[i])
    return result

def drawOhlcvLineGragh(timestamp, openVal, high, low, closeVal, volume, baseCurrency):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('timestamp (s)')
    ax1.set_ylabel(baseCurrency)
    ln1 = ax1.plot(timestamp, openVal, color="green", linewidth=0.6, alpha=0.7, label="open")
    ln2 = ax1.plot(timestamp, high, color="purple", linewidth=0.6, alpha=0.7, label="high")
    ln3 = ax1.plot(timestamp, low, color="gray", linewidth=0.6, alpha=0.7, label="low")
    ln4 = ax1.plot(timestamp, closeVal, color="red", linewidth=0.6, alpha=0.7, label="close")
    #ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    ax2.set_ylabel('volume', color='blue')  # we already handled the x-label with ax1
    ln5 = ax2.plot(timestamp, volume, color='blue', linewidth=0.6, alpha=0.7, label="volume")
    ax2.tick_params(axis='y', labelcolor='blue')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    lns = ln1+ln2+ln3 + ln4 + ln5
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)

    plt.show()

def drawCandleStickChart(timestamp, openVal, high, low, closeVal, volume, exchange, symbol):
    # create two plots
    ax = fplt.create_plot(exchange + '-' + symbol, rows=1)

    # plot candle sticks
    candles = [timestamp, openVal, closeVal, high, low]
    fplt.candlestick_ochl(candles, ax=ax)

    # # put an MA on the close price
    # fplt.plot(timestamp, closeVal.rolling(25).mean(), ax=ax, legend='ma-25')

    # overlay volume on the top plot
    volumes = [timestamp, openVal, closeVal, volume]
    fplt.volume_ocv(volumes, ax=ax.overlay())

    # restore view (X-position and zoom) if we ever run this example again
    fplt.autoviewrestore()

    # we're done
    fplt.show()
