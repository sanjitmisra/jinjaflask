#this file contains the view functions
from flask import render_template, flash, redirect
from app import app
from app.forms import NotesForm

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
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},
		{
			'name' : 'Sherlock Holmes',
			'address' : {'type' : 'Home' ,'line1': '221B Baker St', 'line2' : 'London NW1 6XE'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		},

		{
			'name' : 'James Moriarty',
			'address' : {'type' : 'Office', 'line1': 'Widegate Street', 'line2' : 'London E1 7ES'}
		}
	]

	return render_template('index.html', title='Home', user=user, userdata=userdata)

# Notes Controller
@app.route('/notes')
def notes():
	form = NotesForm()
	return render_template('note.html', title='Meeting Note', form=form)