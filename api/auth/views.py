from flask_restx import Namespace, Resource, fields

auth_namespace = Namespace('auth', description='Namespace for Authentication')

auth_model = auth_namespace.model(
	'User',{
		'id': fields.Integer(),
		'username': fields.String(),
	}
)

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
