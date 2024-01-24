import mysql.connector
import pandas as pd

df = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python_Projects/IMBD_movie/imdb_movie_data_2023.csv")



MyDB = mysql.connector.connect(
	host='localhost',
	user='root',
	password='1234',
	database='trial',
	charset='utf8')

MyCursor = MyDB.cursor()




