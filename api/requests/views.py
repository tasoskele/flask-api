from flask_restx import Namespace, Resource

request_namespace = Namespace('requests', description='Namespace for Requests')

@request_namespace.route('/requests')
class RequestReadCreate(Resource):
	
	def get(self):
		"""
		Get all requests
		"""		
		pass
	
	def post(self):
		"""
		Insert a new request
		"""
		
		pass

@request_namespace.route('/request/<int:request_id>')
class RequestGetUpdateDelete(Resource):
	
	def get(self, request_id):
		"""
		Get a single request
		"""
		pass
	
	def put(self, request_id):
		"""
		Update a request with id
		"""
		pass
	
	def delete(self, request_id):
		"""
		Delete a request with id
		"""
		pass

@request_namespace.route('/user/<int:user_id>/request/<int:request_id>')
class GetUserRequest(Resource):
	
	def get(self, user_id, request_id):
		"""
		Get a request of a user
		"""
		pass

@request_namespace.route('/user/<int:user_id>/requests')
class UserRequests(Resource):
	
	def get(self, user_id):
		"""
		Get all requests of a user
		"""
		pass

@request_namespace.route('/request/status/<int:request_id>')
class UpdateRequestStatus(Resource):
	
	def patch(self, request_id):
		"""
		Update a request's status
		"""
		pass