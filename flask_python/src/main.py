from flask import *
from connection_factory import *

app = Flask(__name__)

@app.route("/")
def index():
    tasks = get_all_table("tasks")
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    state = request.form.get('state')
    if state == 'True':
        state = True
    else:
        state= False
    
    insert_values("Tasks", "name, state", (name, state))

    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete(id):
    delete_recordById("tasks",id)
    return redirect(url_for('index'))


@app.route('/edit/<string:id>')
def edit(id):
    name = "editado"
    state = False
    update_recordById("tasks",id,"name=%s, state=%s",(name, state))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()