import os
from decouple import config

class Config:
	SECRET_KEY=config('SECRET_KEY', 'secret')

class DevConfig(Config):
	DEBUG=config('DEBUG', True)

class TestConfig(Config):
	pass

class ProdConfig(Config):
	pass

config_dict = {
	'dev': DevConfig,
	'prod': ProdConfig,
	'test': TestConfig
}