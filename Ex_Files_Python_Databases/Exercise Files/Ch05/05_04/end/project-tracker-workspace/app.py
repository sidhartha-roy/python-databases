from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_projects():
	return render_template("index.html")

@app.route("/project/<project_id>")
def show_tasks(project_id):
	return render_template("project-tasks.html", project_id=project_id)

@app.route("/add/project", methods=['POST'])
def add_project():
	#Add project
	return "Project added sucessfully"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
	#Add task
	return "Task added successfully"

app.run(debug=True, host="127.0.0.1", port=3000)