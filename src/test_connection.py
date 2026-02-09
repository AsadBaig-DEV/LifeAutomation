import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

SHEET_NAME = os.getenv('GOOGLE_SHEET_NAME')

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

try:
    sheet = client.open(SHEET_NAME).sheet1
    print(f"Connection Successful, '{SHEET_NAME}' Sheet is readable")
except Exception as e:
    print(f"Connection Failed: {e}")