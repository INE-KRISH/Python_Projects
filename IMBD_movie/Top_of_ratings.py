import pandas as pd
import mysql.connector as mysql

MyDB = mysql.connect(
    host='localhost',
    user='root',
    password='12345',
    database='kaggle',
    charset='utf8'
)
MyCursor = MyDB.cursor(buffered=True)
MyCursor.execute("select distinct Genre from imbd_movie;")
MyDB.commit()
MyCursor.close()
MyDB.close()
print("got the genre")