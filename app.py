print('app.py: Importing packages...')
import os
from flask import session, request, render_template, Flask, redirect
from user import User, logged_in
import db as database
os.system('clear')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fjFsdfja2$ffa'
db = database.Db()
non_login_paths = ['/login', '/favicon.ico', 'static/style.css']

# Runs BEFORE any request is completed
@app.before_request
def before_request():

	# If the user is not logged in and he's not going to the login page, redirect him to the login page.
	if logged_in(session) and request.path not in non_login_paths or '/login?redirect=/' not in request.path:
		return redirect('/login?redirect=' + str(request.path))

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/favicon.ico")
def favicon():
	return redirect('http://suanlab.com/assets/images/lecture/python.jpg')
app.run(host='0.0.0.0', port='8080')