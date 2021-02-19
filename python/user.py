
import os
from python.db import Db


db = Db()


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def validate(self):
		users = db.view_users()
		try:
			return users[self.username]['password'] == self.password
		except:
			return False

		






	
def logged_in(session):
	try:
		return session.get('login')[1] == True
	except:
		return False
