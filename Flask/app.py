from flask import Flask
'''
It creates an isntance of the Flask class, 
which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask course."

@app.route('/index')
def index():
    return "Welcome to the index page."


if __name__ == '__main__':
    app.run(debug = True)