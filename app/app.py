from flask import Flask


def create_app():
	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_db.sqlite3'
	# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	from .database import db, create_db
	db.init_app(app)
	create_db(app)


	""" VIEWS """
	from .views.index import index_bp
	app.register_blueprint(index_bp)

	from .views.api import posts_api_bp
	app.register_blueprint(posts_api_bp)

	return app
