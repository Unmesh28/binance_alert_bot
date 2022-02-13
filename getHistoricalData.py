from pydoc import cli
from traceback import print_tb
#from turtle import shape
from wsgiref.util import setup_testing_defaults
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
from datetime import datetime, timedelta    
import settings
from sendTelegramMessage import send_message
from getInterval import getInterval
from getPreviousDateString import getPreviousDateString

client = Client(settings.binanceApiKey, settings.binanceSecret)

def getPreviousData(ticker, interval, candles):
    new_interval = getInterval(interval)
    previousDateString = getPreviousDateString(interval, candles)
    historical = []
    try:
        historical = client.get_historical_klines(ticker, new_interval, previousDateString)
        print(previousDateString)
    
        historical_df = pd.DataFrame(historical)

        historical_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 
                            'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

    except: 
        print("Some error from binance API [Ticker must be delisted]")
   
    if historical_df.empty:
        print('DataFrame is empty!')
    else :
        find_if_fibonacci(historical_df, candles, ticker, interval)
        #fib(historical_df, 40)

def find_if_fibonacci(df, candles, ticker, interval):
        df = df.iloc[-candles::]
        temp = df["Close"].astype(float)
        # ind = (temp/temp.cummin())[(temp/temp.cummin()) == (temp/temp.cummin()).max()].index[0]
        # mini = temp.loc[:ind].min()
        # maxi = temp.loc[ind]
        low = float(min(df['Low']))
        high = float(max(df['High']))   
        mini = float(df['Close'].min())
        maxi = float(df['Close'].max()) 
        maxValueIndex = df['Close'].astype(float).idxmax()
        minValueIndex = df['Close'].astype(float).idxmin()
        print(maxi)
        print(mini)
        difference = maxi - mini
        if(minValueIndex < maxValueIndex) :
            range_min = maxi - difference * 0.67
            range_max = maxi - difference * 0.6
            print(temp.iloc[-1])
            if temp.iloc[-1] >= range_min and temp.iloc[-1] <= range_max:
                message = "Alert: Fibonacci Retracement [LONG] \nSymbol :"+ticker+"\nInterval : "+interval+"\nThe high level is "+str(high)+", the low level is "+str(low)+"\nThere is a Fibonacci Retracement at present level of "+str(temp.iloc[-1])+"\n0.6 Level : "+str(range_max)+" \n0.67 Level : "+str(range_min)
                for chat_id in settings.token_chatID_dict:
                    send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])
            else :
                print('Not Found')
        else :
            range_max = mini + difference * 0.67
            range_min = mini + difference * 0.6
            print(temp.iloc[-1])
            if temp.iloc[-1] >= range_min and temp.iloc[-1] <= range_max:
                message = "Alert: Fibonacci Retracement [SHORT] \nSymbol :"+ticker+"\nInterval : "+interval+"\nThe high level is "+str(high)+", the low level is "+str(low)+"\nThere is a Fibonacci Retracement at present level of "+str(temp.iloc[-1])+"\n0.6 Level : "+str(range_min)+" \n0.67 Level : "+str(range_max)
                for chat_id in settings.token_chatID_dict:
                    send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])
            else :
                print('Not Found')



def fib(df, candles):
    df = df.iloc[-candles::]
    for i in range(1, df.shape[0] - 1):
        print(df['High'][i])



