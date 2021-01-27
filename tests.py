import templates.user
from app import db
print('tests.py: Succesfully imported.\ntests.py: Running...')


print('tests.py: Updating users...')
templates.user.update(db)
print('tests.py: Updated!')


