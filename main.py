from flask import Flask
from routers import task

app = Flask(__name__)


app.register_blueprint(task.blueprint)
