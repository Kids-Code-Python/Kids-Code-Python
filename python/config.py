from os import environ
from flask import Flask
from flask_bootstrap import Bootstrap
import logging
from python.tests import BasicTestCase
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='tests/log.txt')
# To dissable a logging level:
#logging.disable(logging.LEVEL)

def create_app():
	app = Flask(__name__)
	Bootstrap(app)

	

	app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

	return app


class Config:
	log = logging
	app = create_app()
	db_key = environ.get('DB_KEY')
	basic_test = BasicTestCase()
	basic_test.setup()
	
