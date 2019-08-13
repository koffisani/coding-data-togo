import sqlite3

class Db:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method """
        if Db.__instance == None:
            Db()
        return Db.__instance

    def __init__(self):
        if Db.__instance != None:
            raise Exception ('Ceci est un singleton')
        else:
            self.conn = sqlite3.connect('db/test.db')
            self.c = self.conn.cursor()
        
            #c.execute('''
            #    DROP TABLE scraped 
            #''')
            self.c.execute('''
                CREATE TABLE IF NOT EXISTS scraped (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, url text, content text, site text
                )
            ''')

            Db.__instance = self

    def close_connection (self):
        self.conn.close()

