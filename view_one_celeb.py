import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for
app = Flask(__name__)

@app.route('/view_one_celeb')
def view ():
    photo = ''
    celebID=None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    bio = ''
    
    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY photo''')
    rows = c.fetchall()
    conn.close()
    return render_template('view_one_celeb.htm', celebID=celebID, firstname = firstname, lastname = lastname, age=age, email=email, photo=photo, bio=bio)
    
