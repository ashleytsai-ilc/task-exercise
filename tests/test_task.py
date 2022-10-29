import pytest
from http import HTTPStatus


def test_list_tasks(client):
    """
    測試任務列表
    """
    response = client.get("/tasks")
    assert response.status_code == HTTPStatus.OK

def test_create_task(client):
    """
    測試建立任務
    """
    response = client.post("/task",
        json={"name": "買早餐"})
    assert response.status_code == HTTPStatus.CREATED

def test_update_task(client):
    """
    測試更新任務
    """
    response = client.put("/task/1",
        json={"id": 1, "name": "買早餐", "status": 1})
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(("query_id", "id", "name", "status", "msg", "status_code"), (
    (1, 2, "買早餐", 1, "id not match", HTTPStatus.UNPROCESSABLE_ENTITY),
    (100, 100, "買早餐", 1, "task id: 100 not found", HTTPStatus.NOT_FOUND),
))
def test_update_task_invalid_input(client, query_id, id, name, status, msg, status_code):
    """
    測試更新任務非法輸入
    """
    response = client.put(f"/task/{query_id}",
        json={"id": id, "name": name, "status": status})
    assert response.status_code == status_code
    assert response.json["msg"] == msg

def test_delete_task(client):
    """
    測試刪除任務
    """
    response = client.delete("/task/1")
    assert response.status_code == HTTPStatus.OK

def test_delete_task_invalid_input(client):
    """
    測試刪除任務非法輸入
    """
    response = client.delete("/task/100")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json["msg"] == "task id: 100 not found"
