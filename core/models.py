from core import db
from uuid import uuid4

def get_uuid():
    return uuid4().hex

class ToDoList(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=get_uuid)
    todo_description = db.Column(db.String(32), nullable=False)
    is_done = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, todo_description, is_done=False):
        self.todo_description = todo_description
        self.is_done = is_done

def todo_dict(todo):
    return {
        "id": todo.id,
        "todo_description": todo.todo_description,
        "is_done": todo.is_done
    }
