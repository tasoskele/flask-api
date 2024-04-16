from ..utils import db
from enum import Enum

# class Priority:
# 	LOW = 'low'
# 	MEDIUM = 'medium'
# 	HIGH = 'high'

# class RequestStatus:
# 	PENDING = 'pending'
# 	APPROVED = 'approved'
# 	REJECTED = 'rejected'

class Request(db.Model):
	__tablename__ = 'requests'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(255), nullable=False)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
	status = db.Column(db.String(20), default='pending')
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return f"<Request {self.title}>"