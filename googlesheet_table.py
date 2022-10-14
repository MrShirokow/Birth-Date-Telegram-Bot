import pygsheets
import datetime
import config

from pygsheets.client import Client


class GoogleTable:
    def __init__(self, credence_service_file: str = "", googlesheet_file_url: str = ""):
        self.credence_service_file: str = credence_service_file
        self.googlesheet_file_url: str = googlesheet_file_url

    def _get_googlesheet_by_url(self, googlesheet_client: Client) -> pygsheets.Spreadsheet:
        sheets = googlesheet_client.open_by_url(self.googlesheet_file_url)
        return sheets.sheet1

    def _get_googlesheet_client(self) -> Client:
        return pygsheets.authorize(service_file=self.credence_service_file)

    def search_names(self, time_delta: int = 0, name_column: int = 1, date_column: int = 2) -> dict | None:
        search_date = (datetime.date.today() + datetime.timedelta(days=time_delta)).strftime('%d.%m')
        names = {search_date: []}
        googlesheet_client: Client = self._get_googlesheet_client()
        worksheet: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            found_cells = worksheet.find(search_date, matchEntireCell=True, cols=(date_column, date_column))
        except:
            return None
        if not found_cells:
            return None
        for cell in found_cells:
            row = cell.row
            name = worksheet.get_value((row, name_column))
            names[search_date].append(name)     
        return names
