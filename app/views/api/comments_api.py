from flask import Blueprint, jsonify, request
from app.database import db, Comment

comments_api_bp = Blueprint('comments_api', __name__)


@comments_api_bp.route('/comments', methods=["GET"])
def get_comments():
	comments = [{'id': c.id, 'postId': c.postId, 'name': c.name, 'email': c.email, 'body': c.body}
				for c in Comment.query.all()]
	return jsonify(comments), 200


@comments_api_bp.route('/comments', methods=["POST"])
def add_comment():
	new_comment_json = request.json
	try:
		new_comment = Comment(**new_comment_json)
		db.session.add(new_comment)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@comments_api_bp.route('/comments', methods=["PUT"])
def update_comment():
	comment_to_update_json = request.json
	comment_to_update_id = comment_to_update_json.get('id', None)

	if not comment_to_update_id:
		return '', 400

	try:
		comment_to_update = Comment.query.filter_by(id=comment_to_update_id).scalar()
		comment_to_update.postId = comment_to_update_json.get('postId', None)
		comment_to_update.name = comment_to_update_json.get('name', None)
		comment_to_update.email = comment_to_update_json.get('email', None)
		comment_to_update.body = comment_to_update_json.get('body', None)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@comments_api_bp.route('/comments', methods=["DELETE"])
def delete_comment():
	comment_to_delete_id = request.json.get('id', None)

	if not comment_to_delete_id:
		return '', 400

	try:
		comment_to_delete = Comment.query.filter_by(id=comment_to_delete_id).scalar()
		db.session.delete(comment_to_delete)
	except:
		return '', 400

	db.session.commit()
	return '', 200
