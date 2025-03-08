from flask import Flask, request
from todo import Todo

app = Flask(__name__)

@app.route('/tasks', methods = ['POST'])
def create_task():
    data = request.json
    Todo(data).create_task()
    return {"success": True}, 201

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    status = request.args.get("status")
    if status:
        data = Todo({"status": status}).get_task()
    else:
        data = Todo().get_task()
    return {"success": True, "tasks": data}, 200

@app.route('/tasks/<task_id>', methods = ['GET'])
def get_sub_tasks(task_id):
    status = request.args.get("status")
    if status:
        data = Todo({"status": status, "task_id": task_id}).get_subtasks()
    else:
        data = Todo({"task_id": task_id}).get_subtasks()
    return {"success": True, "tasks": data}, 200

@app.route('/tasks/<task_id>', methods = ['DELETE'])
def delete_task(task_id):
    Todo({"task_id": task_id}).delete_task()
    return {"success": True, "message": "Task deleted"}, 200

@app.route('/tasks/<task_id>', methods = ['PUT'])
@app.route('/tasks/<task_id>/status', methods = ['PATCH'])
def update_task(task_id):
    data = request.json
    data.update({"task_id": task_id})
    Todo(data).update_task()
    return {"success": True, "message": "Task Updated"}, 200


@app.route('/tasks/<task_id>/subtask', methods = ['POST'])
def create_subtask(task_id):
    data = request.json
    data.update({"task_id": task_id})
    Todo(data).create_subtask()
    return {"success": True}, 201

@app.route('/tasks/<task_id>/subtask', methods = ['PUT'])
@app.route('/tasks/<task_id>/subtask/<subtask_id>/status', methods = ['PATCH'])
def update_subtask(task_id, subtask_id):
    data = request.json
    data.update({"subtask_id": subtask_id, "task_id": task_id})
    Todo(data).update_subtask()
    return {"success": True, "message": "Task Updated"}, 200

if __name__ == "__main__":
    app.run(debug=True)