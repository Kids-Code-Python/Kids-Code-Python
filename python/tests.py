import unittest
from flask import current_app
from python.config import Config

class BasicsTestCase(unittest.TestCase):
	def setup(self):
		self.app = Config.app
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.log = Config.log
		self.db = Config.db

	
	