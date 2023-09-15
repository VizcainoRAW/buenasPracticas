from flask import Flask, render_template
from connection_factory import *

app = Flask(__name__)

@app.route("/")
def index():
    tasks = get_all_table("tasks")
    return render_template('listas.html', tasks=tasks)

if __name__ == "__main__":
    app.run()