from http import HTTPStatus
from flask import Flask
from flask_pydantic import validate

from schema import TaskStatus
from schema.response import MultiResponse, Response
from schema.response.task import Task
from schema.request.task import CreateTask

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

@app.route("/task", methods=["POST"])
@validate(on_success_status=HTTPStatus.CREATED)
def create_task(body: CreateTask):
    """
    建立任務
    """
    task = {"id": len(tasks) + 1, "name": body.name, "status": TaskStatus.INCOMPLETE}
    tasks.append(task)

    return Response[Task](result=task)
