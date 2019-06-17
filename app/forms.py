from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired

class NotesForm(FlaskForm):
	meetingwith = StringField('Meeting With', validators=[DataRequired()])
	date = DateField('Date', validators=[DataRequired()])
	notes = TextAreaField('Notes', validators=[DataRequired()])
	submit = SubmitField('Save')
