import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread


credentials_path = 'keys.json'
googlesheet_name = 'Binance search parameters'

def readFromGoogleSpreadSheet(credentials_path, sheet_name):
    
    #Define Scope
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    #Google authentication using key.json
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)

    filter_sheet = client.open(googlesheet_name)
    sheet_instance = filter_sheet.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    ticker_df = pd.DataFrame.from_dict(records_data)
    print(ticker_df)


readFromGoogleSpreadSheet(credentials_path, googlesheet_name)
    