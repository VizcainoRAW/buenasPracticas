from flask import *
from config import session
from models.task import *

task_scope = Blueprint("tasks", __name__)

tasks = []

@task_scope.route("/")
def index():
    global tasks
    tasks = session.query(Task).all()
    return render_template("tasks.html", tasks=tasks)


@task_scope.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    state = request.form.get('state')
    if state == 'True':
        state = True
    else:
        state= False
    
    if name and state:
        session.add(Task(name,state))
        session.commit()

    return redirect(url_for('tasks.index'))

@task_scope.route('/delete/<int:task_index>')
def delete(task_index):
    
    task_index-=1
    task=tasks[task_index]

    if task:
        session.delete(task)
        session.commit()
    else:
        print(f"Task with ID {task.id} not found")

    return redirect(url_for('tasks.index'))



@task_scope.route('/edit', methods=["POST"])
def edit():
    id = request.form['id']
    name = request.form['name']
    if request.form.get('state') == 'True':
        state = True
    else:
        state= False

    try:
        task = session.query(Task).filter_by(id=id).first()
        if task:
            if name is not None:
                task.name = name
                task.state = state
            session.commit()
        else:
            print(f"Didn't find a task with id: {id}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return redirect(url_for('tasks.index'))
