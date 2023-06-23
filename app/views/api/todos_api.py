from flask import Blueprint, jsonify, request
from app.database import db, Todo

todos_api_bp = Blueprint('todos_api', __name__)


@todos_api_bp.route('/todos', methods=["GET"])
def get_todos():
	todos = [{'id': t.id, 'userId': t.userId, 'title': t.title, 'completed': t.completed}
			 for t in Todo.query.all()]
	return jsonify(todos), 200


@todos_api_bp.route('/todos', methods=["POST"])
def add_todo():
	new_todo_json = request.json
	try:
		new_todo = Todo(**new_todo_json)
		db.session.add(new_todo)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@todos_api_bp.route('/todos', methods=["PUT"])
def update_todo():
	todo_to_update_json = request.json
	todo_to_update_id = todo_to_update_json.get('id', None)

	if not todo_to_update_id:
		return '', 400

	try:
		todo_to_update = Todo.query.filter_by(id=todo_to_update_id).scalar()
		todo_to_update.userId = todo_to_update_json.get('userId', None)
		todo_to_update.title = todo_to_update_json.get('title', None)
		todo_to_update.body = todo_to_update_json.get('body', None)
		todo_to_update.completed = todo_to_update_json.get('completed', None)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@todos_api_bp.route('/todos', methods=["DELETE"])
def delete_todo():
	todo_to_delete_id = request.json.get('id', None)

	if not todo_to_delete_id:
		return '', 400

	try:
		todo_to_delete = Todo.query.filter_by(id=todo_to_delete_id).scalar()
		db.session.delete(todo_to_delete)
	except:
		return '', 400

	db.session.commit()
	return '', 200
