__all__ = [
	'Post',
	'Album',
	'Comment',
	'Todo'
]

from . import db


class Post(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	userId = db.Column(db.Integer, nullable=False)
	title = db.Column(db.String(64))
	body = db.Column(db.String(256))

	def __repr__(self):
		return f'<Post: id={self.id}, userId={self.userId}, title={self.title}, body={self.body}>'


class Album(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	userId = db.Column(db.Integer, nullable=False)
	title = db.Column(db.String(64))


class Comment(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	postId = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(64))
	email = db.Column(db.String(64))
	body = db.Column(db.String(256))


class Todo(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	userId = db.Column(db.Integer, nullable=False)
	title = db.Column(db.String(64))
	completed = db.Column(db.Boolean)
