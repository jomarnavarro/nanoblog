from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
	user = {'username': 'Omar'}
	posts = [
		{
			'author': {'username': 'omar'},
			'body': 'Today was a sunny day in Mexico City'
		},
		{
			'author': {'username': 'chank'},
			'body': 'A poor politician is a lousy politician'
		},
		{
			'author': {'username': 'csalinas'},
			'body': 'I hear no evil and see no evil.'
		}
	]
	return render_template('index.html', title='Index', user=user, posts=posts)

@app.route('/login', methods = ["GET", "POST"])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data
		))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
