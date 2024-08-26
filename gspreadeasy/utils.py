import gspread
import pandas as pd
from google.oauth2 import service_account

class GoogleSheetClient:

    def __init__(self, conn_json, sheet_id):
        scope = ["https://spreadsheets.google.com/feeds"]
        credentials = service_account.Credentials.from_service_account_file(conn_json, scopes=scope)
        self.client = gspread.authorize(credentials)
        self.sheet_id = sheet_id

    def get_data_from_googlesheet(self, sheet_name: str) -> list:
        wks = self.client.open_by_key(self.sheet_id).worksheet(sheet_name)
        self.df = pd.DataFrame(wks.get_all_records())
        return self 
    
    def show_data(self):
        return self.df

    def override_data_in_googlesheet(self, sheet_name: str, df = None):
        #check if we gave a DF 
        if df is None:
            df = self.df
        #check if sheet exists
        #otherwise create it 
        #get the list of worksheets names 
        names = [sheet.title for sheet in self.client.open_by_key(self.sheet_id).worksheets()]
        if sheet_name not in names:
            self.client.open_by_key(self.sheet_id).add_worksheet(title=sheet_name, rows=1000, cols=20)
        #add our df as the content of the sheet
        wks = self.client.open_by_key(self.sheet_id).worksheet(sheet_name)
        wks.clear()
        wks.update([df.columns.values.tolist()] + df.values.tolist())
        print('Updated sheet: ' + sheet_name)