import sqlite3

# The connect function will create a database here.
# If the database exists then the connect function will connect
# to the already created movies database
connection = sqlite3.connect('movies.db')

# to create a table we need to grab the cursor object
# with the cursor object we will be able to create
# command and queries to the database
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
        (Title TEXT, Director TEXT, YEAR INT)''')

connection.commit()
connection.close()
