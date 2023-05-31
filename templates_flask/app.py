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
def animaliList():
        mycursor.execute("""SELECT id, animal_name, hair, feathers, eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,venomous,fins,legs,tail,domestic,catsize,class_type, descrizione 
        FROM Animali, gruppo 
        WHERE class_type = nome_gruppo""")
        myresult = mycursor.fetchall()
        return render_template('animali.html', surename=myresult)

@app.route('/predator')
def predatorList():
        mycursor.execute("SELECT * FROM Animali")
        myresult = mycursor.fetchall()
        return render_template('animali.html', predator=myresult)