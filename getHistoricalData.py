binanceApiKey = 'E3Tzfl1rtOyljmVTjxvsW1az9k7uXVYelrmsPcBwfHyy2ulwWQiT3IxSeOawpwwH'
binanceSecret = '2FtDBi6y2WYi8Pp32ScDSYSm28uRkHg1LJMXSaLxEQJi88o4Fr1Z8uWuBhSihWX2'

from pydoc import cli
from traceback import print_tb
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
from datetime import datetime, timedelta    

client = Client(binanceApiKey, binanceSecret)

historical = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1HOUR, '8 Feb 2022')
historical_df = pd.DataFrame(historical)

historical_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 
                            'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
print(historical_df.head())


def find_if_fibonacci1(df):
        print(df)
        temp = df["Close"].astype(float)
        mini = float(min(df['Low']))
        maxi = float(max(df['High']))   
        print(mini)
        print(maxi)
        range_min = maxi - (maxi-mini)*0.67
        range_max = maxi - (maxi-mini)*0.6
        print(range_min)
        print(range_max)
        print(temp.iloc[-1])
        if temp.iloc[-1] >= range_min and temp.iloc[-1] <= range_max:
            message = "Alert: Fibonacci Retracement \nSymbol :"+symbol+"\nInterval : 1H\nThe high level is "+str(maxi)+", the low level is "+str(mini)+"\nThere is a Fibonacci Retracement at present level of "+str(temp.iloc[-1])
            print(message)
        else :
            print('Not Found')

find_if_fibonacci1(historical_df)
