from flask_restx import Namespace, Resource

requests_namespace = Namespace('requests', description='Namespace for Requests')

@requests_namespace.route('/')
class HelloRequests(Resource):
	def get(self):
		return {'message': 'Hello from Requests'}
