from flask import Flask, render_template, request, redirect, url_for
from connection_factory import *

app = Flask(__name__)

@app.route("/")
def index():
    tasks = get_all_table("tasks")
    return render_template("index.html", tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form['name']
    state = request.form.get('state', False)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()