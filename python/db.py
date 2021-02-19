from requests import get
from python.config import Config


class Db:
	def __init__(self):
		self.app = Config.app
		self.log = Config.log
		self.key = Config.db_key
	class session:
		def start():
			get('https://Kids-Code-Python-DB-API.isaiah08.repl.co/')