from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    priority = SelectField('Priority', choices=['Low', 'Medium', 'High'], validators=[DataRequired()])
    submit = SubmitField('Submit')