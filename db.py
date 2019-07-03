import sqlite3

class Db:

    conn = sqlite3.connect('db/test.db')

    c = conn.cursor()
    
    #c.execute('''
    #    DROP TABLE scraped 
    #''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS scraped (
            id INTEGER PRIMARY KEY AUTOINCREMENT, url text, content text, site text
        )
    ''')

