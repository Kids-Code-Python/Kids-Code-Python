print('app.py: Importing packages...')
import os
from flask import session, request, render_template, Flask, redirect
from flask_bootstrap import Bootstrap


from python.forms import *
from python.user import logged_in
import python.db as database
from python.forms import LoginForm
os.system('clear')
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'fjFsdfja2$ffa'
db = database.Db()


non_login_paths = ['/login', '/favicon.ico', '/static/style.css', '/test']

# Runs BEFORE any request is completed
@app.before_request
def before_request():
	from python import tests
	tests.test(app)


	# If the user is not logged in and he's not going to the login page, redirect him to the login page.
	if logged_in(session) == False and request.path not in non_login_paths or '/login' not in request.path:
		return redirect('/login?redirect=' + str(request.path))

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])


def login():
	form = LoginForm()
	if form.validate_on_submit():
		ip_address = request.remote_addr
		username = form.username.data
		password = form.password.data
		print('User with IP of ' + str(ip_address) + 
		'logged in')

	return render_template('login.html')

@app.route("/favicon.ico")
def favicon():
	return redirect('http://suanlab.com/assets/images/lecture/python.jpg')
app.run(host='0.0.0.0', port='8080')