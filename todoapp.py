from flask import Flask, render_template, flash, redirect
from config import Config
from forms import AddTaskForm

app = Flask(__name__)
app.config.from_object(Config)

todo_list_items = [
        {
            'email': 'wilson@email.com',
            'task': 'take out trash'
        },
        {
            'email': 'wilson@email.com',
            'task': 'wash dishes'
        }
    ]

@app.route('/', methods=['GET', 'POST'])

def index():
    
    form = AddTaskForm()

    return render_template('index.html', items=todo_list_items, form=form)

@app.route('/submit', methods=['GET', 'POST'])

def submit():
    form = AddTaskForm()

    if form.validate_on_submit():
        flash(f'Adding task: "{form.task_name.data}" for {form.email.data}.')
        data = form
        return render_template('index.html', items=todo_list_items, form=form, data=data)
    else: 
        return render_template('index.html', items=todo_list_items, form=form)

# @app.route('/clear')

if __name__ == '__main__':
    app.run()

# FLASK_APP=todoapp.py FLASK_ENV=development flask run - allows for debug mode, hot reload.