import settings
from readSpreadSheet import readFromGoogleSpreadSheet
from getHistoricalData import getPreviousData

tickers = readFromGoogleSpreadSheet(settings.credentials_path, settings.googlesheet_name)
#getPreviousData('BTTUSDT')
for ticker in tickers:
    print(ticker)
    getPreviousData(ticker)