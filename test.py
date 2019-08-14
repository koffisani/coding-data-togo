from db import Db
import os

db_file = 'db/test_db.db'
instance_1 = Db.getInstance(db_file)
instance_2 = Db.getInstance(db_file)

def test_open_connection():
    assert os.path.exists(db_file) == True, "Devrait être True"

def test_Db ():
    assert instance_1 == instance_2, "Devrait être " + instance_1

    # sélection 
    cursor = instance_1.conn.cursor()
    data = cursor.execute("SELECT COUNT(*) FROM scraped")
    values = data.fetchone()

    assert values[0] == 0, "Devrait être 0"

def test_close_connection():
    instance_1.close_connection()
    instance_1.remove_db()
    assert os.path.exists(db_file) == False, "Devrait être false"