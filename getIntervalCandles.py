from matplotlib import ticker
from numpy import rec
import settings 
from readSpreadSheet import readFromGoogleSpreadSheet
import pandas as pd

def getCandles(interval, sheetIndex):
    try : 
        records_data = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name, 2)
        ticker_df = pd.DataFrame.from_dict(records_data)
        #ticker_df = pd.DataFrame(eval(records_data))
        #print("*************", ticker_df[interval][sheetIndex])
        return ticker_df[interval][sheetIndex] 
    
    except :
        return 0
        
          




