from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from LoginManager import LoginManager
import CONSTANTS
from Book import Book
from Library import Library

app = Flask(__name__)
app.secret_key = 'lol beka'


@app.route('/')
def homepage():

		library_books = Library(CONSTANTS.LIBRARY_TABLE)

		return render_template('template.html', books=library_books.books)


@app.route('/login')
def login():
        return render_template('login.html')


@app.route('/admin')
def admin():
        return render_template('admin.html')


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

		return 'Zapisano, kurwiu'
	else:
		return 'Nie kombinuj...'



@app.route('/verify-login', methods = ['POST'])
def verify_login():

	login_status = LoginManager.authenticate(request.form['username'], request.form['password'])
	
	if login_status != CONSTANTS.LOGIN_FAILED:
		session['username'] = request.form['username']

		if login_status == CONSTANTS.LOGIN_ADMIN:
			session['user_type'] = 'admin'
		else:
			session['user_type'] = 'client'

		return 'logged in'
	else:
		return 'fail'
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
