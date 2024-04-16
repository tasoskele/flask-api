from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth', description='Namespace for Authentication')

@auth_namespace.route('/signup')
class SignUp(Resource):
	def post(self):
		return {'message': 'Sign Up'}