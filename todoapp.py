from flask import Flask, render_template, flash, request, redirect
from config import Config
from forms import AddTaskForm

app = Flask(__name__)
app.config.from_object(Config)

todo_list_items = [
        {
            'email': 'wilson@email.com',
            'task': 'take out trash',
            'priority': 'Low'
        },
        {
            'email': 'wilson@email.com',
            'task': 'wash dishes',
            'priority': 'Low'
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
        new_item = {
            'email': form.email.data,
            'task': form.task_name.data,
            'priority': form.priority.data
        }
        todo_list_items.append(new_item)
        render_template('index.html', items=todo_list_items, form=form, data=data)
        return redirect('/')
    else: 
        return render_template('index.html', items=todo_list_items, form=form)


@app.route('/clear')

def clear():
    todo_list_items.clear()
    form = AddTaskForm()

    render_template('index.html', items=todo_list_items, form=form)
    return redirect('/')

if __name__ == '__main__':
    app.run()

# FLASK_APP=todoapp.py FLASK_ENV=development flask run - allows for debug mode, hot reload.