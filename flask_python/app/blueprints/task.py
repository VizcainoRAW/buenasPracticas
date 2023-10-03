from flask import *
from .conf import *

task_scope = Blueprint("tasks", __name__)


@task_scope.route("/")
def index():
    tasks = get_all_table("tasks")
    template_folder = current_app.jinja_loader.searchpath[0]
    print(f'Ubicación de la carpeta de plantillas: {template_folder}')
    return render_template("tasks.html", tasks=tasks)

@task_scope.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    state = request.form.get('state')
    if state == 'True':
        state = True
    else:
        state= False
    
    insert_values("Tasks", "name, state", (name, state))

    return redirect(url_for('index'))

@task_scope.route('/delete/<id>')
def delete(id):
    delete_recordById("tasks",id)
    return redirect(url_for('index'))


@task_scope.route('/edit',methods=["POST"])
def edit():
    id =request.form['id']
    name = request.form['name']
    state = request.form.get('state')
    update_recordById("tasks",id,"name=%s, state=%s",(name, state))
    return redirect(url_for('index'))