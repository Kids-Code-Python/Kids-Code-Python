import os
class User:
	def __init__(self, username, password, db, session):
		self.username = username
		self.password = password
		self.db = db
		self.session = session
	def create(self, occupation):
		os.system(str('export ' + 'user_' + self.username + '=' + self.password))
		self.db[[self.username, 'user']] = {'occupation':occupation, 'classes': [], 'projects': []}
	def delete(self):
		del self.db[[self.username, 'user']]
		os.environ.pop(str('export ' + 'user_' + self.username + '=' + self.password))
	def create_class(self, name, description, lessons):
		user = self.db[[self.username, 'user']]
		user['classes'].append({'name': name, 'description': description,
		'lessons': lessons})
	def create_project(self, project_name, description):
		pass
	def logged_in(self):
		try:
			return self.session.get('login')[1] == True
		except:
			return False