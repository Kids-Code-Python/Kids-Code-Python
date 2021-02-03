import os

def logged_in(session):
	try:
		return session.get('login')[1] == True
	except:
		return False