import mysql.connector
import pandas as pd


#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()


#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASSIFICA_ANIMALI_ZOO")


mycursor.execute("DROP TABLE IF EXISTS CLASSIFICA_ANIMALI_ZOO.curiosita")


#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS CLASSIFICA_ANIMALI_ZOO.curiosita (
    nome_animali VARCHAR(30) NOT NULL,
    descrizione_curiosita TEXT
  );""")


#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM CLASSIFICA_ANIMALI_ZOO.curiosita")
mydb.commit()


#Read data from a csv file
Animali_data = pd.read_csv('./Curiosita.csv', index_col=False, delimiter = ',')
Animali_data = Animali_data.fillna('Null')


print(Animali_data.head(20))


#Fill the table
for i,row in Animali_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values
    sql = "INSERT INTO CLASSIFICA_ANIMALI_ZOO.curiosita VALUES (%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()


mycursor.execute("SELECT * FROM CLASSIFICA_ANIMALI_ZOO.curiosita")
myresult = mycursor.fetchall()






for x in myresult:
  print(x)






