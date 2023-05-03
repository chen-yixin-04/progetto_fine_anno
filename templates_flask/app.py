from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASSIFICA_ANIMALI_ZOO"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def pilotiList():
        mycursor.execute("SELECT * FROM Animali")
        myresult = mycursor.fetchall()
        return render_template('aniamli.html', surename=myresult)

@app.route('/units')
def pilotiList():
        mycursor.execute("SELECT * FROM Animali")
        myresult = mycursor.fetchall()
        return render_template('aniamli.html', surename=myresult)