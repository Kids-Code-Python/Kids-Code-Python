import requests
import os

API_KEY = str(os.getenv('API_KEY'))

class Db:
	def view_users(self):
		return requests.get('https://Kids-Code-Python-API.isaiah08.repl.co/' + API_KEY + '/users/view')
	def add_user(self, name, occupation):
		return requests.get('https://Kids-Code-Python-API.isaiah08.repl.co/' + API_KEY + 'users/add?name=' + name + '&occupation='+ occupation)