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

def add_new_project(cursor, project_title, project_description, 
	task_descriptions):
	project_data = (project_title, project_description)
	cursor.execute('''INSERT INTO projects(title, description) 
		VALUES (%s, %s)''', project_data)

	project_id = cursor.lastrowid

	tasks_data = []

	for description in task_descriptions:
		task_data = (project_id, description)
		tasks_data.append(task_data)

	cursor.executemany('''INSERT INTO tasks(project_id, description)
		VALUES (%s, %s)''', tasks_data)

if __name__ == '__main__':
	db = connect("projects")
	cursor = db.cursor()

	tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
	add_new_project(cursor, "Clean house", "Clean house by room", tasks)
	db.commit()

	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)

	cursor.execute("SELECT * FROM tasks")
	tasks_records = cursor.fetchall()
	print(tasks_records)

	db.close()





