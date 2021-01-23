import os

def update(db):
	for user, data in db.items():
		if user[1] == 'user':
			try:
				user_file = open('users/'+user[0],'r')
				
			except FileNotFoundError:
				print(user[0] + 'not found:\nCreating file...')
				user_file = open('user/' + user[0] + '.txt', 'xt')