from flask import Flask,request
from app.database import task


app = Flask(__name__) 

@app.get("/task")
def get_all_task():
    task_list = task.scan()
    out = {
        "ok":True,
        "task":task_list
    }
    return out

    @app.get("/task/<int:pk>")
    def get_task_by_id(pk):
        single_task = task.select_by_id(pk)
        out = {
            "ok":True,
            "task":single_task
        }
        return out


@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    out = {
        "ok":True,
        "message":"Task Created"
    }
    return out, 201

    @app.put("/task/<int:pk>")
    def update_task(pk):
        task_data = request.json
        task.update_by_id(task_data, pk)
        return "", 204

@app.delete("/task/<int:pk>")
def delete_task(pk):
    task.delete_task_by_id(pk)
    return "",204