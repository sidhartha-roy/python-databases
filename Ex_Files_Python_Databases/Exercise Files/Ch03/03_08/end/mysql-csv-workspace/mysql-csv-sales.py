import mysql.connector as mysql
import csv

connection = mysql.connect(user='root',
	password='password',
	host='localhost',
	database='sales',
	allow_local_infile=True)

cursor = connection.cursor()

create_query = '''CREATE TABLE salesperson(
	id INT(255) NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email_address VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
	state VARCHAR(255) NOT NULL,
	PRIMARY KEY (id))'''

cursor.execute("DROP TABLE IF EXISTS salesperson")

cursor.execute(create_query)

# with open('./salespeople.csv', 'r') as f:
# 	csv_data = csv.reader(f)
# 	for row in csv_data:
# 		print(row)
# 		row_tuple = tuple(row)
# 		cursor.execute('INSERT INTO salesperson(first_name, last_name, email_address, city, state) VALUES("%s", "%s", "%s", "%s","%s")', row_tuple)

q = '''LOAD DATA LOCAL INFILE 
'/Users/author/desktop/mysql-csv-workspace/salespeople.csv'
 INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
 (first_name, last_name, email_address, city, state);'''

cursor.execute(q)

connection.commit()

cursor.execute("SELECT * FROM salesperson LIMIT 10")
print(cursor.fetchall())

connection.close()







