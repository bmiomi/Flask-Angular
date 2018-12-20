import os
class Config(object):
	SECRET_KEY= 'miomi'

class DevelopmentConfig(Config):
	DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd ()) + "/flask1.db"	
	SQLALCHEMY_ECHO=False
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	TRAP_BAD_REQUEST_ERRORS = True
