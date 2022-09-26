from flask import Flask, render_template
import sqlite3
import os

# create a new flask app
app = Flask(__name__)

# create a function that will be called when the user accesses the root of the website
def get_db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) # create connection to the database
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/patients')
def patients_list():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql:', patientListSql)
    return render_template('index.html', listPatients=patientListSql) #creating variable listPatients in .html that contains sql data (patientsListSql) from sqlite db

@app.route('/bootstrap')
def bootstrap():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('bootstrap.html', listPatients=patientListSql) # note, these are two variables, patientsList is what we can then look up in the .html, and the patientsListSql is the actual data we are pulling from the sqlite db


if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=80)