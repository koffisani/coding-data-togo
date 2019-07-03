import sqlite3

class Db:

    def __init__(self):
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

    def close_connection (self):
        self.conn.close()

