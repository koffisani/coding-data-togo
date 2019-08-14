import sqlite3
import os

class Db:

    __instance = None
    __db_file = 'db/database.db'

    @staticmethod
    def getInstance(file=None):
        """ Static access method """
        if Db.__instance == None:
            if file != None:
                Db.__db_file = file
            Db()
        return Db.__instance

    def __init__(self):
        if Db.__instance != None:
            raise Exception ('Ceci est un singleton')
        else:
            self.conn = sqlite3.connect(self.__db_file)
            self.c = self.conn.cursor()
        
            self.c.execute('''
                CREATE TABLE IF NOT EXISTS scraped (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, url text, content text, site text
                )
            ''')

            Db.__instance = self

    def close_connection (self):
        self.conn.close()

    def remove_db (self):
        if os.path.exists(self.__db_file):
            os.remove(self.__db_file)


