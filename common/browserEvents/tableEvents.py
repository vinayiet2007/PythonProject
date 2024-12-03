from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from common.interfaces.iTableActions import ITableActions
from common.utilities.logger import Logger

class TableActions(ITableActions):

    def __init__(self,driver,table:WebElement):
        self.driver = driver
        self.table = table

    def count_rows(self):
        try:
            rows = self.table.find_elements(By.TAG_NAME, "tr")
            row_count = len(rows)
            return row_count
        except Exception as e:
            Logger.critical(f"Exception found in fetching rows : {e}")

    def select_row(self,row_num:int):
        try:
            rows = self.table.find_elements(By.TAG_NAME, "tr")
            self.driver.click(rows[row_num])
        except Exception as e:
            Logger.critical(f"Exception found in selecting on row_num {row_num} rows : {e}")

    def read_table_row(self,row_num:int):
        try:
            rows = self.table.find_elements(By.TAG_NAME, "tr")
            self.driver.text(rows[row_num])
        except Exception as e:
            Logger.critical(f"Exception found in reading table row on row_num {row_num} rows : {e}")

    def read_column_data_by_id(self,col_num:int):
        try:
            rows = self.table.find_elements(By.TAG_NAME, "tr")
            column_data = []
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, "td")
                column_data.append(cells[col_num].text)
            return column_data
        except Exception as e:
            Logger.critical(f"Exception found in reading table column on col_num {col_num} rows : {e}")

    def read_cell_data_by_id(self,row_num:int,col_num:int):
        try:
            row = self.table.find_elements(By.TAG_NAME, "tr")[row_num]
            cells = row.find_elements(By.TAG_NAME, "td")
            return cells[col_num].text
        except Exception as e:
            Logger.critical(f"Exception found in reading table cell on row_num {row_num} and on col_num {col_num} rows : {e}")