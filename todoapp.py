from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World! This is a To-Do List app!'

# @app.route('/submit')

# @app.route('/clear')

if __name__ == '__main__':
    app.run()

# FLASK_APP=todoapp.py FLASK_ENV=development flask run - allows for debug mode, hot reload.