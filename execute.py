import settings
from readSpreadSheet import readFromGoogleSpreadSheet
from getHistoricalData import getPreviousData

def execute(interval):
    tickers = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name)
    #getPreviousData('BTTUSDT')
    for ticker in tickers:
        getPreviousData(ticker, interval)


# execute('1h')
# execute('4h')