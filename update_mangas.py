import gspread
from oauth2client.service_account import ServiceAccountCredentials
from manga_bot import mangabot

class MangaUpdater(object):
    def __init__(self, spreadsheet_name):
        self.manga_col = 1
        self.directory_url = 2
        self.chapter = 3
        self.chapter_url = 4

        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

        #Include your JSON file
        creds = ServiceAccountCredentials.from_json_keyfile_name('.....json', scope)

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def process_manga_list(self):
        mangas = self.sheet.col_values(self.manga_col)[1:]

        manga_bot = mangabot(mangas)
        directory_urls, chapter, chapter_urls = manga_bot.search_manga()

        print("Updating spreadsheet.")
        for i in range(len(chapter)):
            self.sheet.update_cell(i+2, self.directory_url, directory_urls[i])
            self.sheet.update_cell(i+2, self.chapter, chapter[i])
            self.sheet.update_cell(i+2, self.chapter_url, chapter_urls[i])
    

manga_updater = MangaUpdater("...") #INCLUDE YOUR SPREADSHEET NAME MADE ON GOOGLE DRIVE
manga_updater.process_manga_list()

