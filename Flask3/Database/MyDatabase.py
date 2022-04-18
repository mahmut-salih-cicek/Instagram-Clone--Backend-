

import sqlite3
import json
import numpy as np



vt = sqlite3.connect('person00.db', check_same_thread=False )
im = vt.cursor()


def createDatabase():
    im.execute("CREATE TABLE IF NOT EXISTS personel (listid INTEGER PRIMARY KEY ,email ,realName , password, userName )")
    print("Database created")

def insertDatabase(email,realName,password,userName):
    im.execute("INSERT INTO personel VALUES (?,?,?,?,?);", (None,email,realName,password,userName ))
    vt.commit()

def showDatabase():
    im.execute("SELECT * FROM personel")
    veriler = im.fetchall()
    #vt.close()
    print(veriler)
    #return json.dumps(veriler)
    return veriler

def searchEmail(email):
    bool = "false"

    im.execute("SELECT * FROM personel WHERE email = '%s'" % email)
    #im.execute("SELECT * FROM personel WHERE email like '%s'" % email)

    veri = list(im.fetchall())
    print(len(veri))
    size = len(veri)
    if size >=1:
        final_result = [list(i) for i in veri]
        print("bbbbbb")
        print(final_result[0][1])
        result = final_result[0][1]
        if result == email:
            bool = "true"

    return bool





