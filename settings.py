import readSpreadSheet

credentials_path = 'keys.json'
googlesheet_name = 'Binance search parameters'

readSpreadSheet.readFromGoogleSpreadSheet(credentials_path, googlesheet_name)