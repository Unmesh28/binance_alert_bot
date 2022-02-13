import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def readFromGoogleSpreadSheet(credentials_path, sheet_name, sheet_no):
    
    #Define Scope
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    #Google authentication using key.json
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)

    filter_sheet = client.open(sheet_name)
    sheet_instance = filter_sheet.get_worksheet(sheet_no)
    records_data = sheet_instance.get_all_records()
    return records_data
    
    