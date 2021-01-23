import templates.user
from app import db


print('Updating users...')
templates.user.update(db)
print('Updated!')

