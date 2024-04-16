from flask import Flask
from flask_restx import Api
from .requests.views import requests_namespace
from .auth.views import auth_namespace

def create_app():
	app = Flask(__name__)

	return app