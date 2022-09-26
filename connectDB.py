#import needed modules 
import pandas as pd 
import sqlite3

## testing if the db works
def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# saves the data to a dataframe using pandas
df = pd.DataFrame(patientListSql)
df

# renames the columns to the names given in the orginal file
df.columns = ['mrn', 'firstname', 'lastname', 'gender', 'dob', 'city', 'insurance', 'phone']
df