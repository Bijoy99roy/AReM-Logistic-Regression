# performing important imports
from datetime import datetime
from db_operations.database import DataBase


class AppLogger:
    def __init__(self):
        try:
            self.database = DataBase()
        except Exception as e:
            raise e

    def create_table(self):
        try:
            self.database.create_tables()
        except Exception as e:
            raise e

    def log(self, table_name, message, level=''):
        try:
            now = datetime.now()
            date = now.date()
            current_time = now.strftime('%H:%M:%S')
            self.database.insert_data(table_name, date, current_time, message, level)
        except Exception as e:
            raise e
