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

mycursor.execute("DROP TABLE IF EXISTS CLASSIFICA_ANIMALI_ZOO.Animali")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS CLASSIFICA_ANIMALI_ZOO.Animali (
    id integer, 
    animal_name VARCHAR(30) NOT NULL,
    hair Boolean ,
    feathers Boolean,
    eggs Boolean,
    milk Boolean,
    airborne Boolean,
    aquatic Boolean,
    predator Boolean,
    toothed Boolean,
    backbone Boolean,
    breathes Boolean,
    venomous Boolean,
    fins Boolean,
    legs Integer,
    tail Boolean,
    domestic Boolean,
    catsize Boolean,
    class_type Integer
    
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM CLASSIFICA_ANIMALI_ZOO.Animali")
mydb.commit()

#Read data from a csv file
Animali_data = pd.read_csv('./zoo.csv', index_col=False, delimiter = ',')
Animali_data = Animali_data.fillna('Null')

print(Animali_data.head(20))

#Fill the table
for i,row in Animali_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO CLASSIFICA_ANIMALI_ZOO.Animali VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM CLASSIFICA_ANIMALI_ZOO.Animali")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)