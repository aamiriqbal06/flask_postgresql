from flask import Flask, render_template, request, redirect
from db import tasklist_db, add_task

app = Flask(__name__)

@app.route("/")
def hello_world():
    TaskList_db  = tasklist_db()
    print(tasklist_db()) 
    return (render_template("index.html",Tasklist_db=TaskList_db))

@app.route("/add",methods=["POST"])
def add():
    if request.method == "POST":
        task=request.form["task"]
        date=request.form["date"]
        add_task(task,date)
        return redirect("/")

if __name__ == "__main__": 
    app.run(debug=True)