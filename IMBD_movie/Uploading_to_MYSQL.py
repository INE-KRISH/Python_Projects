import mysql.connector
import pandas as pd

df = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python_Projects/IMBD_movie/imdb_movie_data_2023.csv")

# Replace NaN values with "-"
df = df.fillna("-")

MyDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='kaggle',
    charset='utf8'
)

MyCursor = MyDB.cursor()

# Check the data types and update the placeholders accordingly
sql = (
    "INSERT INTO IMBD_Movie "
    "(S_no, Moive_Name, Rating, Votes, Meta_Score, Genre, PG_Rating, Year, Duration, Cast, Director) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

# Iterate over rows in the DataFrame and execute the insert statement for each row
for index, row in df.iterrows():
    # Replace NaN values with "-"
    row = row.fillna("-")
    MyCursor.execute(sql, tuple(row))

# Commit changes to the database
MyDB.commit()

# Close the cursor and connection
MyCursor.close()
MyDB.close()

print("Records inserted")

