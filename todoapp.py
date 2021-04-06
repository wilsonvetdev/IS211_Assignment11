from flask import Flask, render_template, flash, request, redirect
from config import Config
from forms import AddTaskForm, ClearTasksForm

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
    clear_form = ClearTasksForm()
    return render_template('index.html', items=todo_list_items, form=form, clear_form=clear_form)



@app.route('/submit', methods=['GET', 'POST'])

def submit():
    form = AddTaskForm()
    clear_form = ClearTasksForm()

    if form.validate_on_submit():
        flash(f'Adding task: "{form.task_name.data}" for {form.email.data}.')
        data = form
        new_item = {
            'email': form.email.data,
            'task': form.task_name.data,
            'priority': form.priority.data
        }
        todo_list_items.append(new_item)
        render_template('index.html', items=todo_list_items, form=form, clear_form=clear_form, data=data)
        return redirect('/')
    else: 
        return render_template('index.html', items=todo_list_items, clear_form=clear_form, form=form)


@app.route('/clear', methods=['POST'])

def clear():
    todo_list_items.clear()
    form = AddTaskForm()
    clear_form = ClearTasksForm()

    render_template('index.html', items=todo_list_items, form=form, clear_form=clear_form)
    return redirect('/')

if __name__ == '__main__':
    app.run()

# FLASK_APP=todoapp.py FLASK_ENV=development flask run - allows for debug mode, hot reload.