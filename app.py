from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from LoginManager import LoginManager
import CONSTANTS
from Book import Book
from Library import Library
from DatabaseConnection import DatabaseConnection as DC

app = Flask(__name__)
app.secret_key = 'something'


@app.route('/')
def homepage():

		library_books = Library(CONSTANTS.LIBRARY_TABLE)

		return render_template('template.html', books=library_books.books)


@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/register')
def register():
        return render_template('register.html')


@app.route('/admin')
def admin():
		library_books = Library(CONSTANTS.LIBRARY_TABLE)

		return render_template('admin.html', books=library_books.books)

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
			return redirect(url_for('admin'))
		else:
			session['user_type'] = 'client'
			return redirect(url_for('client'))
	else:
		return redirect(url_for('login'))
    
@app.route('/log-out')
def log_out():

	session.clear()
	return redirect(url_for('login'))

@app.route('/delete/<key>')
def delete_book(key):
	DC.delete_data('/library', key)
	return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
