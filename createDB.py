import sqlite3 

#connect to sqlite
connect = sqlite3.connect('patients.db')


db = connect.cursor()

# delete table patient_table if it exists in patients.db
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit() #see if change happened after execute command


#creating patients table
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            city CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL,
            phone CHAR(25) NOT NULL
        ); """

#calling table variable via db.execute
db.execute(table)
connect.commit() #commit changes

#insert dummy data into table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance, phone) values('12345', 'John', 'Smith', 'M', '01/01/2000', 'New York', 'United Health', '3472130987')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance, phone) values('23456', 'Jane', 'Doe', 'F', '02/02/2001','New York', 'CIGNA', '6467651290')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance, phone) values('34567', 'Mary', 'Smith', 'F', '03/03/2002','New York', 'Caresource', '9171239876')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance, phone) values('45678', 'Bob', 'Smith', 'M', '04/04/2003','New York', 'United Health', '6311234567')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, gender, dob, city, insurance, phone) values('56789', 'Jess', 'Doe', 'F', '05/05/2004','New York', 'Metropolitan', '9786352145')")

connect.commit() #commit changes


# close the connection
connect.close()