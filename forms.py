from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class AddTaskForm(FlaskForm):
    task_name = StringField('To Do Item', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    priority = SelectField('Priority', choices=['Low', 'Medium', 'High'], validators=[DataRequired()])
    submit = SubmitField('Add To Do Item')

class ClearTasksForm(FlaskForm):
    submit = SubmitField('Clear To-Do List')