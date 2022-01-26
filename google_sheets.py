from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account


def get_sheet(ID, JSON):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = JSON

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,scopes = SCOPES
    )


    SAMPLE_SPREADSHEET_ID = ID
    SAMPLE_RANGE_NAME = 'Linky!A2:C121'

    creds = credentials

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            pass

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('Žiadne dáta.')
            return


    except HttpError as err:
        print(err)

    """service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])"""




    return values #IGNOROVAŤ



"""kokot = get_sheet('114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM',"eshop-sheet-c38c9c8a59ed.json")

print(kokot[0:4])
print(kokot[4:8])

nums = [[0,4],[4,8]]

for x in range(nums[0][0],nums[0][1]):
    print(kokot[x])"""
