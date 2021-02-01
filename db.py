def real_db(db):
	new_db = {}
	for k, v in db.items():
		if k.isupper() == False:
			new_db[k] = v
	return new_db
