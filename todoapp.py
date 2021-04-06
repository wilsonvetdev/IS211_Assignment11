from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():

    todo_list_items = [
        {
            'person': 'Wilson',
            'task': 'take out trash'
        },
        {
            'person': 'Wilson',
            'task': 'wash dishes'
        }
    ]

    return render_template('index.html', items=todo_list_items)

# @app.route('/submit')

# @app.route('/clear')

if __name__ == '__main__':
    app.run()

# FLASK_APP=todoapp.py FLASK_ENV=development flask run - allows for debug mode, hot reload.