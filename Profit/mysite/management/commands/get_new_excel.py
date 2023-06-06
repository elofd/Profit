import os

from django.core.management import BaseCommand
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Настройки таблицы Google
        SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
        RANGE_NAME = 'Sheet1'

        # Настройки файла Excel на сервере
        SERVER_FILE_PATH = 'mysite.xlsx'

        # Настройки авторизации в Google API
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

        # Авторизация в Google API
        creds = None
        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # Получение данных из таблицы Google
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(
                spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        # Запись данных в файл Excel
        if values:
            df = pd.DataFrame(values[1:], columns=values[0])
            df.to_excel('mysite.xlsx', index=False)

        # Замена файла Excel на сервере
        if os.path.exists('mysite.xlsx'):
            os.replace('mysite.xlsx', SERVER_FILE_PATH)
