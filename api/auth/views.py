from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth', description='Namespace for Authentication')

@auth_namespace.route('/signup')
class SignUp(Resource):
	
	def post(self):
		"""
		Create a new user
		"""
		pass

@auth_namespace.route('/login')
class Login(Resource):
	
	def post(self):
		"""
		Login a user - Generate JWT
		"""		
		pass
