from flask import request,jsonify
from core import app,db
from .models import ToDoList,todo_dict

@app.route('/todo',methods=['GET'])
def get_todo():
    todos=ToDoList.query.order_by(ToDoList.id.asc()).all()
    todo_list=[todo_dict(todo) for todo in todos]
    return jsonify(todo_list), 200


@app.route('/todo/<string:id>',methods=['GET'])
def get_todo_by_id(id):
    todo=ToDoList.query.filter_by(id=id).first()
    return jsonify(todo_dict(todo)), 200

@app.route('/todo',methods=['POST'])
def create_todo():
    data=request.get_json()
    todo_description=data.get('todo_description')
    is_done=data.get('is_done',False)
    new_todo=ToDoList(todo_description=todo_description,is_done=is_done)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(todo_dict(new_todo)), 200



@app.route('/todo/<string:id>',methods=['PUT'])
def update_todo_by_id(id):
    data=request.get_json()
    todo_description=data.get('todo_description')
    is_done=data.get('is_done',False)
    todo=ToDoList.query.filter_by(id=id).first()
    if todo_description:
        todo.todo_description=todo_description
    if "is_done" in data:
        todo.is_done=is_done
    db.session.commit()
    return jsonify(todo_dict(todo)), 200



@app.route('/todo/<string:id>',methods=['DELETE'])
def delete_todo_by_id(id):
    todo=ToDoList.query.filter_by(id=id).first()
    if not todo:
        return jsonify({'msg':'You dindt found this todo'})
    db.session.delete(todo)
    db.session.commit()
    return jsonify(todo_dict(todo)), 200
