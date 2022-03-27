import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

# cursor.execute("SELECT * FROM Movies")

# famous_films = [('Pulp Fiction', 'Quintin Tarantino', 1994), 
        # ('Back to the Future', 'Stephen Spielberg', 1985),
        # ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famous_films)

records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchone())
print(cursor.fetchall())

for record in records:
    print(record)

connection.commit()
connection.close()
