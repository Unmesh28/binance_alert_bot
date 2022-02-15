from curses import window
from email import message
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
import talib as ta


client = Client(settings.binanceApiKey, settings.binanceSecret)

def getPreviousData(ticker, interval, candles, strategy):
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
        if (strategy == 'fib') :
            find_if_fibonacci(historical_df, candles, ticker, interval)
        elif (strategy == 'bba') :
            bollinger_bands(historical_df, candles, ticker, interval)


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


def construct_bollinger_message(ticker, interval, upper_or_lower) :
    initial_text = "Alert : Bolinger Band \n"
    symbol_text = "Symbol : " +ticker + "\n"
    interval_text = "Interval : "+interval+"\n"  
    signal_text = "Signal : Out of"+ upper_or_lower + " band"
    messgage = initial_text + symbol_text + "\n" + interval_text + signal_text 
    return messgage

def bollinger_bands(df, candles, ticker, interval):
    upper,middle,lower = ta.BBANDS(df.Close[-candles::],timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
    #print(upper)
    df['Upper'] = upper
    df['Lower'] = lower
    print(ticker)
    print(df['Upper'].iloc[-1])
    print(df['Close'].iloc[-1])
    if (float(df['Close'].iloc[-1]) > float(df['Upper'].iloc[-1])) :
        #print("Out of upper band")
        message = construct_bollinger_message(ticker, interval, " upper")
        for chat_id in settings.token_chatID_dict:
            send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])
    elif (float(df['Close'].iloc[-1]) < float(df['Lower'].iloc[-1])) :
        #print("Out of lower band")
        message = construct_bollinger_message(ticker, interval, " lower")
        for chat_id in settings.token_chatID_dict:
            send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])
    




