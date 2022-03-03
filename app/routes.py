from flask import render_template
from flask import render_template
from app import app

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

