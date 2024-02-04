import pandas as pd
import mysql.connector as mysql
MyDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='kaggle',
    charset='utf8'
)

df = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python_Projects/IMBD_movie/imdb_movie_data_2023.csv")
df1 = list(set(df['Genre']))
mycur = MyDB.cursor()
for i in range(len(df1)):
    x = df[i,'Genre']


