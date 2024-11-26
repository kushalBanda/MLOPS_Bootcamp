from flask import Flask, render_template
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
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)