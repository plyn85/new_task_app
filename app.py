from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
import os
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
  return redirect(url_for("add_task"))
@app.route('/get_tasks')
def get_tasks():
  # this aims back at the tasks html and page and the mongo db database
# we use the find function with mongo db to fetch our tasks
    return render_template("tasks.html",
                           tasks=mongo.db.tasks.find())


@app.route('/add_task')
# this aims back at the addtask html and page and the mongo db database
# we use the find function with mongo db to fetch our categories
def add_task():
    return render_template('addtask.html',
                            categories=mongo.db.categories.find() 


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
