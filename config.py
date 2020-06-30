import os


# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'Thisisasecret!'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secretPassword@mysqlDB:3306/db_flask_app'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
