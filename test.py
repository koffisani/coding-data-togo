from db import Db

def test_Db ():
    instance_1 = Db.getInstance()
    instance_2 = Db.getInstance()

    assert instance_1 == instance_2, "Devrait être " + instance_1

if __name__ == '__main__':
    test_Db()
    print ("Exécution terminée.")