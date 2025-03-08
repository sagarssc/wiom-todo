
from db import Mysql

class Todo(Mysql):
    
    def __init__(self, data = {}):
        self.data = data
        Mysql.__init__(self)
    
    def create_task(self):
        self.data.update({"status": "pending"})
        self.create("tasks", self.data)
        return
    
    def get_task(self):
        result = self.get("tasks")
        return result
    
    def get_subtasks(self):
        task_id = self.data.get("task_id")
        result = self.get("sub_tasks", {"task_id": task_id})
        return result
    
    def delete_task(self):
        task_id = self.data.get("task_id")
        query = f"Delete from Tasks where id = {task_id}"
        self.raw_query(query)
        return
    
    def update_task(self):
        task_id = self.data.pop("task_id")
        self.update("tasks", self.data, {"id": task_id})
        return
    
    def create_subtask(self):
        self.data.update({"status": "pending"})
        self.create("sub_tasks", self.data)
        return
    
    def delete_subtask(self):
        task_id = self.data.get("task_id")
        query = f"Delete from sub_tasks where id = {task_id}"
        self.raw_query(query)
        return
    
    def update_subtask(self):
        task_id = self.data.pop("task_id")
        subtask_id = self.data.pop("subtask_id")
        self.update("sub_tasks", self.data, {"id": subtask_id, "task_id": task_id})
        return