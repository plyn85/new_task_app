# from bson.object import ObjectId
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
import os
from os import path
if path.exists("env.py"):
    import env
    # bson  is used to  convert the ID that's been
    # passed across from our template into a
    # readable format that's acceptable by MongoDB.
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
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
                           categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
# Now, because we're submitting a form, and we're submitting using POST,
# we must refer to the HTTP method that will be used to deliver the form data.
# in this case its post the default is get
def insert_task():
    # the first line will get the tasks collection from the mongo db database
    # the second line will submit infomation to a web location in the form of a request object
    #  inside that we say show me the form
    # we converted it to a dictonary so it can easily be understood by mongo
    #  any of the form fields that have data inside them will be submitted to the tasks collection in mongodb
    #  during thr project from validation shoul be used and in add tasks html section
    #  the last line will redirect to get/tasks function  above so we can veiw the new task in our mongo db collection
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
# adding function to connect to the edit task button here
# In order to do do this we need to retrive the task from the data base
#  we want to find one particular task from our tasks collection

# Where looking for a match the _id the key in mongo
# We put the tasks_Id parameter in a format that exceptable to mongo
# we use the mongo db find function to grab categories


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_task.html', task=the_task,
                           categories=all_categories)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
