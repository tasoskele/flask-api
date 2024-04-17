from ..utils import db
from enum import Enum

class Sizes(Enum):
	SMALL = 'small'
	MEDIUM = 'medium'
	LARGE = 'large'
	EXTRA_LARGE = 'extra_large'

class RequestStatus(Enum):
	PENDING = 'pending'
	PROCESSING = 'processing'
	COMPLETED = 'completed'

class Request(db.Model):
	__tablename__ = 'requests'

	id = db.Column(db.Integer, primary_key=True)
	size = db.Column(db.Enum(Sizes), default=Sizes.SMALL, nullable=False)
	request_status = db.Column(db.Enum(RequestStatus), default=RequestStatus.PENDING, nullable=False)
	#
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return f"<Request {self.id}>"