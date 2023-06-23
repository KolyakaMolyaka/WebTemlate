from flask import Blueprint, jsonify, request
from app.database import db, Album

albums_api_bp = Blueprint('albums_api', __name__)


@albums_api_bp.route('/albums', methods=["GET"])
def get_albums():
	albums = [{'id': a.id, 'userId': a.userId, 'title': a.title}
			 for a in Album.query.all()]
	return jsonify(albums), 200


@albums_api_bp.route('/albums', methods=["POST"])
def add_album():
	new_album_json = request.json
	try:
		new_album = Album(**new_album_json)
		db.session.add(new_album)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@albums_api_bp.route('/albums', methods=["PUT"])
def update_post():
	album_to_update_json = request.json
	album_to_update_id = album_to_update_json.get('id', None)

	if not album_to_update_id:
		return '', 400

	try:
		album_to_update = Album.query.filter_by(id=album_to_update_id).scalar()
		album_to_update.userId = album_to_update_json.get('userId', None)
		album_to_update.title = album_to_update_json.get('title', None)
		album_to_update.body = album_to_update_json.get('body', None)
	except:
		return '', 400

	db.session.commit()
	return '', 200


@albums_api_bp.route('/albums', methods=["DELETE"])
def delete_album():
	album_to_delete_id = request.json.get('id', None)

	if not album_to_delete_id:
		return '', 400

	try:
		album_to_delete = Album.query.filter_by(id=album_to_delete_id).scalar()
		db.session.delete(album_to_delete)
	except:
		return '', 400

	db.session.commit()
	return '', 200
