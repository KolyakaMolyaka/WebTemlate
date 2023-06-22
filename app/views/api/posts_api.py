from flask import Blueprint, jsonify, request
from app.database import db, Post

posts_api_bp = Blueprint('posts_api', __name__)


@posts_api_bp.route('/posts', methods=["GET"])
def get_posts():
	posts = [{'id': p.id, 'userId': p.userId, 'title': p.title, 'body': p.body}
			 for p in Post.query.all()]
	return jsonify(posts), 200


@posts_api_bp.route('/posts', methods=["POST"])
def add_post():
	new_post_json = request.json
	try:
		new_post = Post(**new_post_json)
		db.session.add(new_post)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@posts_api_bp.route('/posts', methods=["PUT"])
def update_post():
	post_to_update_json = request.json
	post_to_update_id = post_to_update_json.get('id', None)

	if not post_to_update_id:
		return '', 400

	try:
		post_to_update = Post.query.filter_by(id=post_to_update_id).scalar()
		post_to_update.userId = post_to_update_json.get('userId', None)
		post_to_update.title = post_to_update_json.get('title', None)
		post_to_update.body = post_to_update_json.get('body', None)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@posts_api_bp.route('/posts', methods=["DELETE"])
def delete_post():
	post_to_delete_id = request.json.get('id', None)

	if not post_to_delete_id:
		return '', 400

	try:
		post_to_delete = Post.query.filter_by(id=post_to_delete_id).scalar()
		db.session.delete(post_to_delete)
	except:
		return '', 400

	db.session.commit()
	return '', 200
