import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect(database="red30",
		user="postgres",
		password="password",
		host="localhost",
		port="5432")
	
	cur = conn.cursor()