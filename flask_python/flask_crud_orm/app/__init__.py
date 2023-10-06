from flask import Flask
from blueprints.task import task_scope
import config

app = Flask(__name__)


app.register_blueprint(task_scope, url_prefix='/')


if __name__ == "__main__":
    app.run()