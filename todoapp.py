#Praveen Lama

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

# this works as our db for storing current session tasks
listArr = []


class Task:
    def __init__(self, task, email, priority):
        self.task = task
        self.email = email
        self.priority = priority


@app.route('/')
def showList():
    #t = Task("wash","john","high"); #dummy task to test
    #listArr.append(t);
    return render_template('index.html', listArr=listArr)
#def hello_world():
#    return'HelloWorld!'


@app.route('/submit', methods=['POST'])
def submit():
    # Note: we take care of the invalid input in the front end for better efficiency
    # Validating input in the front end not only takes load off the back end service,
    # but also provides extra security i.e. sql injection etc
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    curr = Task(task, email, priority)
    listArr.append(curr)
    return redirect("/")# redirect to homepage


@app.route('/clear', methods=['POST'])
def clear():
    del listArr[:] # clearing the array storage
    return redirect("/")


if __name__ == '__main__':
    app.run()