import datetime as dt
import time
import datetime
import numpy as np
import pandas as pd
import yfinance as yf

stock_list = [
    'ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS',
    'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'BHARTIARTL.NS', 'BPCL.NS',
    'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DRREDDY.NS',
    'EICHERMOT.NS', 'GAIL.NS', 'GRASIN.NS', 'HELTECH.NS', 'HDFC.NS',
    'HDFCBANK.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS',
    'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS',
    'KOTAKBANK.NS', 'LT.NS', 'HEM.NS', 'MARUTI.NS', 'NESTLEIND.NS',
    'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS',
    'SHREECEM.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS',
    'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS',
    'UPL.NS', 'VEDL.NS', 'WIPRO.NS', 'YESBANK.NS', 'ZEEL.NS']

start = dt.datetime(2024, 1, 1)
now = dt.datetime.now()

while 1:
    alerts = {'Stock': [], "above_20": [], 'cross': []}

    for stock in stock_list:
        df = yf.download(stock, start, now, interval='15m')
        df['20ma'] = df['Adj Close'].rolling(20).mean()
        df['10ma'] = df['Adj Close'].rolling(10).mean()

        df['above_20'] = np.where((df['Adj Close'] > df['20ma'])
                                  & (df['Adj Close'].shift() < df['20ma'].shift()), 1, 0)
        df['cross_over'] = np.where((df['10ma'] > df['20ma'])
                                    & (df['20ma'].shift() < df['10ma'].shift()), 1, 0)

        for i in df.index:
            price_now = df['Adj Close'][i]

            if df['above_20'][i] == 1:
                print("Alert on ", stock, price_now)
                alerts['Stock'].append(stock)
                alerts['above_20'].append(price_now)
                alerts['cross'].append('')
                break

            if df['cross_over'][i] == 1:
                print("Alert on ", stock, price_now)
                alerts['Stock'].append(stock)
                alerts['above_20'].append('')
                alerts['cross'].append(price_now)
                break

    alerts = pd.DataFrame(alerts)
    print(alerts)
    time.sleep(10)



