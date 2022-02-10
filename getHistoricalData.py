from pydoc import cli
from traceback import print_tb
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
from datetime import datetime, timedelta    
import settings
from sendTelegramMessage import send_message
from getInterval import getInterval
from getPreviousDateString import getPreviousDateString

client = Client(settings.binanceApiKey, settings.binanceSecret)

def getPreviousData(ticker, interval):
    new_interval = getInterval(interval)
    previousDateString = getPreviousDateString(interval)
    historical = []
    try:
        historical = client.get_historical_klines(ticker, new_interval, previousDateString)
    
        historical_df = pd.DataFrame(historical)

        historical_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 
                            'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

    except: 
        print("Some error from binance API [Ticker must be delisted]")
   
    if historical_df.empty:
        print('DataFrame is empty!')
    else :
        find_if_fibonacci(historical_df, 40, ticker, interval)

def find_if_fibonacci(df, candles, ticker, interval):
        df = df.iloc[-candles::]
        temp = df["Close"].astype(float)
        mini = float(min(df['Low']))
        maxi = float(max(df['High']))   
        range_min = maxi - (maxi-mini)*0.67
        range_max = maxi - (maxi-mini)*0.6
        print(temp.iloc[-1])
        if temp.iloc[-1] >= range_min and temp.iloc[-1] <= range_max:
            message = "Alert: Fibonacci Retracement \nSymbol :"+ticker+"\nInterval : "+interval+"\nThe high level is "+str(maxi)+", the low level is "+str(mini)+"\nThere is a Fibonacci Retracement at present level of "+str(temp.iloc[-1])
            for chat_id in settings.chat_id_list:
                send_message(chat_id,"sendMessage",message)
                print(message)     
        else :
            print('Not Found')

