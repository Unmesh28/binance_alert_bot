from curses import window
from email import header, message
from pydoc import cli
from traceback import print_tb
from wsgiref.util import setup_testing_defaults
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from momentum import momentum   
import settings
from sendTelegramMessage import send_message
from getInterval import getInterval
from getPreviousDateString import getPreviousDateString
import talib as ta
from support_resistance import support_resistance
from os.path import exists
from getIndex import getIndexPreviousVal, add_cuurent_to_previous
from previous_msg_file import createNewFile
from momentum import momentum
import pandas




client = Client(settings.binanceApiKey, settings.binanceSecret)

def getPreviousDataNew(ticker, interval, candles, strategy):
    new_interval = getInterval(interval)
    previousDateString = getPreviousDateString(interval, candles)
    historical = []
    historical_df = []
    try:
        historical = client.get_historical_klines(ticker, new_interval, previousDateString)
        print(previousDateString)
    
        historical_df = pd.DataFrame(historical)
        #historical_df.transpose()
        #print(historical_df)

        historical_df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume' , 'Close Time', 
                            'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

        # historical_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 
        #                     'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
        print(historical_df)

    except: 
        print("Some error from binance API [Ticker must be delisted]")
        

    historical_df['datetime'] = historical_df.timestamp.apply(
            lambda x: pandas.to_datetime(datetime.fromtimestamp(x / 1000).strftime('%c'))
        )
        # print(historical_df)

    historical_df.set_index('datetime', inplace=True, drop=True)
    historical_df.drop('timestamp', axis=1, inplace=True)
    momentum(historical_df, candles, ticker, interval)


   

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
        return 0
   
    if historical_df.empty:
        print('DataFrame is empty!')
    else :
        if (strategy == 'fib') :
            find_if_fibonacci(historical_df, candles, ticker, interval)
        elif (strategy == 'bba') :
            bollinger_bands(historical_df, candles, ticker, interval)
        elif (strategy == 'sup_res') :
            support_resistance(historical_df, ticker, candles, interval)
        elif (strategy == "momentum") :
            momentum(historical_df, ticker, candles, interval)


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
        previous_msg_file_name = "previous_msg_fib.csv"
        file_exists = exists(previous_msg_file_name)
        print(file_exists)
        if (file_exists == False) :
            createNewFile(previous_msg_file_name)            
            
        index, prevous_value = getIndexPreviousVal(interval, ticker, previous_msg_file_name)
        print(index, prevous_value)
        difference = maxi - mini
        if(minValueIndex < maxValueIndex) :
            range_min = maxi - difference * 0.67
            range_max = maxi - difference * 0.6
            
            print(temp.iloc[-1])
            if temp.iloc[-1] >= range_min and temp.iloc[-1] <= range_max:
                current_value = np.float64("{:.16g}".format(range_max + range_min))
                print(ticker)
                print('Current Value '+str(current_value) )
                print('Previous Value' + str(prevous_value))
                if(prevous_value != current_value) :
                    print(type(prevous_value))
                    print(type(current_value))
                    #print(prevous_value - current_value)
                    add_cuurent_to_previous(current_value, index, interval, previous_msg_file_name)
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
                #current_value = format((range_max + range_min), ".16g")
                current_value = np.float64("{:.16g}".format(range_max + range_min))
                print(ticker)
                print('Current Value '+str(current_value) )
                print('Previous Value' + str(prevous_value))
                if(prevous_value != current_value) :
                    print(type(prevous_value))
                    print(type(current_value))
                    #print(prevous_value - current_value)
                    add_cuurent_to_previous(current_value, index, interval, previous_msg_file_name)
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
    previous_msg_file_name_bba_upper = "bba_upper.csv"
    file_exists1 = exists(previous_msg_file_name_bba_upper)
    print(file_exists1)
    if (file_exists1 == False) :
        createNewFile(previous_msg_file_name_bba_upper)    
    previous_msg_file_name_bba_lower = "bba_lower.csv"
    file_exists2 = exists(previous_msg_file_name_bba_lower)
    print(file_exists2)
    if (file_exists2 == False) :
        createNewFile(previous_msg_file_name_bba_lower)  

    index1, prevous_bba_upper = getIndexPreviousVal(interval, ticker, previous_msg_file_name_bba_upper)
    index2, prevous_bba_lower = getIndexPreviousVal(interval, ticker, previous_msg_file_name_bba_lower)
    upper,middle,lower = ta.BBANDS(df.Close[-candles::],timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
    #print(upper)
    df['Upper'] = upper
    df['Lower'] = lower
    print(ticker)
    print(df['Upper'].iloc[-1])
    print(df['Close'].iloc[-1])
    if (float(df['Close'].iloc[-1]) > float(df['Upper'].iloc[-1])) :
        #print("Out of upper band")
        current_value = np.float64("{:.16g}".format(float(df['Close'].iloc[-1])))
        print(current_value)
        print(prevous_bba_upper)

        if (prevous_bba_upper != current_value):
            add_cuurent_to_previous(current_value, index1, interval, previous_msg_file_name_bba_upper)
            message = construct_bollinger_message(ticker, interval, " upper")
            for chat_id in settings.token_chatID_dict:
                send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])

        
    elif (float(df['Close'].iloc[-1]) < float(df['Lower'].iloc[-1])) :
        #print("Out of lower band")
        current_value = np.float64("{:.16g}".format(float(df['Close'].iloc[-1])))
        if (current_value != prevous_bba_lower) :
            add_cuurent_to_previous(current_value, index2, interval, previous_msg_file_name_bba_lower)
            message = construct_bollinger_message(ticker, interval, " lower")
            for chat_id in settings.token_chatID_dict:
                send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])
        
    




