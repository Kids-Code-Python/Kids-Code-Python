import os
print('user.py: Succesfully imported')

def update(db):
	'Updates user files'
	for user, data in db.items():
		if user[1] == 'user':
			try:
				user_file = open('templates/users/'+user[0] + '.json','r')
				print('user.py: ' + user[0] + ' found. Updating...')

				print('user.py: Updated!')
			except FileNotFoundError:
				print('user.py: ' + user[0] + ' not found:\nCreating file...')
				user_file = open('templates/users/' + user[0] + '.json', 'w')

