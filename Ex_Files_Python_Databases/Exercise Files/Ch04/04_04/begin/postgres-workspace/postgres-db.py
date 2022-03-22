import psycopg2

conn = psycopg2.connect(database="red30",
	user="postgres",
	password="password",
	host="localhost",
	port="5432")

conn.close()