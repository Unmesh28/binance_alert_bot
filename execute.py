import pandas as pd
import settings
from readSpreadSheet import readFromGoogleSpreadSheet
from getHistoricalData import getPreviousData
from getIntervalCandles import getCandles

def execute(interval, strategy):
    records_data = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name, 0)
    ticker_df = pd.DataFrame.from_dict(records_data)
    tickers = ticker_df['tickerName']
    candles = 0
    if(strategy == 'fib') :
        candles =  getCandles(interval, 0)
    
    if candles > 0 :
        for ticker in tickers:
            getPreviousData(ticker, interval, candles)
    
    else :
        print('Candeles are zero fror this interval')

execute('1m', 'fib')
# execute('4h')