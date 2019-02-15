import gspread
from oauth2client.service_account import ServiceAccountCredentials


class MangaUpdater(object):
    def __init__(self, spreadsheet_name):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

manga_updater = MangaUpdater("manga_chapters")



#         stuff = sheet.get_all_records()

# print(stuff)