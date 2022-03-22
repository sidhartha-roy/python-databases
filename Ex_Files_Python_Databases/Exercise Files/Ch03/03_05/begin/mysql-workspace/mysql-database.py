import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(
			host='localhost',
			user='root',
			password='password',
			database=db_name)
	except Error as e:
		print(e)

if __name__ == '__main__':
	db = connect("projects")
	cursor = db.cursor()
	
	db.close()