from matplotlib.pyplot import get
import pandas as pd
import settings
from readSpreadSheet import readFromGoogleSpreadSheet
from getHistoricalData import getPreviousData
from getIntervalCandles import getCandles

def execute(interval, strategy):
    records_data = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name, 0)
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
    
    if candles > 0 :
        for i in one_indices :
            getPreviousData(tickers[i], interval, candles, strategy) 
    else :
        print('Candeles are zero fror this interval')


#execute('12h', 'fib') 
#execute('1h', 'sup_res') 
#execute('4h')