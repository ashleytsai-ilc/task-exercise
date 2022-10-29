from flask import Flask
from flask_pydantic import validate
from schema.response import MultiResponse
from schema.response.task import Task

app = Flask(__name__)


# init task data
tasks = [{"id": 1, "name": "name", "status": 0}]

@app.route("/tasks")
@validate()
def list_tasks():
    """
    取得任務列表
    """
    return MultiResponse[Task](result=tasks)
