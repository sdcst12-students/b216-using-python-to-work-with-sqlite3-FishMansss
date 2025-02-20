#!python

"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

##setup
import sqlite3
file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

#table creation
cursor.execute("CREATE TABLE pet (name tinytext, species tinytext, breed tinytext,  age int, gender tinytext, sn tinytext, id integer primary key autoincrement );")
