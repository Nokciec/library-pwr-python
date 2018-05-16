from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from LoginManager import LoginManager
import CONSTANTS
from Book import Book
from Library import Library
from DatabaseConnection import DatabaseConnection as DC
from User import User as User

app = Flask(__name__)
app.secret_key = 'something'


# Bad global stuff ahead

GlobalLibrary = Library(CONSTANTS.LIBRARY_TABLE)

@app.route('/')
def homepage():

		global GlobalLibrary

		return render_template('template.html', books=GlobalLibrary.books)


@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/register')
def register():
        return render_template('register.html')


@app.route('/admin')
def admin():
		global GlobalLibrary

		return render_template('admin.html', books=GlobalLibrary.books)

@app.route('/client')
def client():
		global GlobalLibrary

		return render_template('client.html', books=GlobalLibrary.books)


@app.route('/add-book', methods = ['POST'])
def add_book():

	if session['user_type'] == 'admin':
		Book.create_new_library_book(
				request.form['title'],
				request.form['author'],
				request.form['ISBN'],
				request.form['publication_date'],
				request.form['publication_place'],
				request.form['publisher'],
				request.form['number_of_pages']
			).save(CONSTANTS.LIBRARY_TABLE)

		return redirect(url_for('admin'))
	else:
		return 'You are not allowed...'


@app.route('/verify-login', methods = ['POST'])
def verify_login():

	login_status = LoginManager.authenticate(request.form['username'], request.form['password'])
	
	if login_status != CONSTANTS.LOGIN_FAILED:
		session['username'] = request.form['username']

		if login_status == CONSTANTS.LOGIN_ADMIN:
			session['user_type'] = 'admin'
			return redirect(url_for('admin'))
		else:
			session['user_type'] = 'client'
			return redirect(url_for('client'))
	else:
		return redirect(url_for('login'))
    
@app.route('/log-out')
def log_out():

	session.clear()
	return render_template('template.html', books=GlobalLibrary.books)

@app.route('/delete/<key>')
def delete_book(key):
	DC.delete_data('/library', key)
	return redirect(url_for('admin'))

@app.route('/rent/<book_id>/<login>')
def rent_book(book_id, login):
	global  GlobalLibrary
	GlobalLibrary.rent_book(book_id, login)
	return redirect(url_for('admin'))

@app.route('/return/<book_id>')
def return_book(book_id):
	global GlobalLibrary
	GlobalLibrary.return_book(book_id)
	return redirect(url_for('admin'))

@app.route('/reserve/<book_id>')
def reserve_book(book_id):
	global GlobalLibrary
	GlobalLibrary.reserve_book(book_id)
	return redirect(url_for('client'))

@app.route('/prolong/<book_id>')
def prolong(book_id):
	global GlobalLibrary
	GlobalLibrary.prolong(book_id)
	return redirect(url_for('client'))

@app.route('/create-account', methods = ['POST'])
def create_account():

	users_data = DC.get_data(CONSTANTS.USERS_TABLE)

	for user_id in users_data:
		user = User.empty()

		user.load(CONSTANTS.USERS_TABLE + '/' + user_id)
		if user.login == request.form['login']:
			return 'User already exists!'
		

	user = User(
			request.form['login'],
			request.form['password'],
			request.form['name'],
			request.form['surname'],
			True if request.form['account_type'] == 'true' else False
		)

	user.save(CONSTANTS.USERS_TABLE)

	return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
