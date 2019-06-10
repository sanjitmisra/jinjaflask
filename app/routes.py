#this file contains the view functions
from flask import render_template
from app import app

#the @app. is a decorator
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'johndoe'}
	userdata = [
		{
			'name' : 'Sherlock Holmes',
			'address' : {'type' : 'Home' ,'line1': '221B Baker St', 'line2' : 'London NW1 6XE'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		}
	]

	return render_template('index.html', title='Home', user=user, userdata=userdata)