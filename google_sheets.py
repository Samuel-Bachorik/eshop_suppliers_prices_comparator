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
    print("Google sheets ready...")


    return values #IGNOROVAŤ

