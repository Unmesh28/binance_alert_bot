from matplotlib.pyplot import get
import pandas as pd
import settings
from readSpreadSheet import readFromGoogleSpreadSheet
from getHistoricalData import getPreviousData, getPreviousDataNew
from getIntervalCandles import getCandles

def execute(interval, strategy):
    records_data = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name, 0)
    if (records_data == 0) :
        return 0
    ticker_df = pd.DataFrame.from_dict(records_data)
    tickers = ticker_df['tickerName']
    index = ticker_df.index
    condition = ticker_df["active"] == 1 
    one_indices = index[condition]
    candles = 0
    if(strategy == 'fib') :
        candles =  getCandles(interval, 0)
    if(strategy == 'bba') : 
        candles = getCandles(interval, 1)
    if(strategy == 'sup_res') : 
        candles = getCandles(interval, 2)
    else : candles = 60
    
    if candles > 0 :
        for i in one_indices :
            getPreviousData(tickers[i], interval, candles, strategy) 
    else :
        print('Candeles are zero fror this interval')

#execute('1h', "momentum")
#execute('1h', 'bba') 
#execute('1h', 'sup_res') 
#execute('4h')
# getPreviousData("ADAUSDT", "1h", 100, "sup_res") 
getPreviousDataNew("BTCUSDT", "5m", 90, "momentum") 
# getPreviousDataNew("BTCUSDT", '1h', 60, 'momentum') 