from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate

from schema import TaskStatus
from schema.response import MultiResponse, Response, ErrResponse
from schema.response.task import Task
from schema.request.task import CreateTask, UpdateTask

blueprint = Blueprint('task', __name__)
# init task data
tasks = [{"id": 1, "name": "name", "status": 0}]


@blueprint.route("/tasks")
@validate()
def list_tasks():
    """
    取得任務列表
    """
    return MultiResponse[Task](result=tasks)


@blueprint.route("/task", methods=["POST"])
@validate(on_success_status=HTTPStatus.CREATED)
def create_task(body: CreateTask):
    """
    建立任務
    """
    task = {"id": len(tasks) + 1, "name": body.name,
            "status": TaskStatus.INCOMPLETE}
    tasks.append(task)

    return Response[Task](result=task)


@blueprint.route("/task/<id>", methods=["PUT"])
@validate()
def update_task(id: int, body: UpdateTask):
    """
    更新任務
    """
    if id != body.id:
        return ErrResponse(msg="id not match"), HTTPStatus.UNPROCESSABLE_ENTITY

    request_task = {}
    for task in tasks:
        if task["id"] == id:
            request_task = body.__dict__
            task.update(request_task)
            break

    if request_task == {}:
        return ErrResponse(msg=f"task id: {id} not found"), HTTPStatus.NOT_FOUND

    return Response[Task](result=request_task)


@blueprint.route("/task/<id>", methods=["DELETE"])
@validate()
def delete_task(id: int):
    """
    刪除任務
    """
    deleted = False
    for i in range(len(tasks)):
        if tasks[i]["id"] == id:
            del tasks[i]
            deleted = True
            break

    if not deleted:
        return ErrResponse(msg=f"task id: {id} not found"), HTTPStatus.NOT_FOUND

    return ""
