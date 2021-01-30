import os
class User:
	def __init__(self, username, password, db):
		self.username = username
		self.password = password
		self.db = db
	def create(self, occupation):
		os.system(str('export ' + 'user_' + self.username + '=' + self.password))
		self.db[[self.username, 'user']] = {'occupation':occupation, 'classes': [], 'projects': []}
	def delete(self):
		del self.db[[self.username, 'user']]
		os.environ.pop(str('export ' + 'user_' + self.username + '=' + self.password))
	def create_class(self, name, description, db):
		user = db[[self.username, 'user']]
		user['classes'].append({'name': name, 'description': description})