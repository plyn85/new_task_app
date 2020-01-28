import os 
from os import path
if path.exists("env.py"):
  import env 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI') 

mongo = PyMongo(app)

@app.route('/')
def index():
  return redirect(url_for("add_task"))
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
