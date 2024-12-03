### Building URL Dynamically
## Variable Rule
### Jinja 2 Template Engine

'''
{{ }} expressions to print output in html
{%.....%} conditions, for loops
{#...#} this is for comments
'''


from flask import Flask, render_template, request, redirect, url_for
'''
It creates an isntance of the Flask class, 
which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask course."

@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    else:
        return render_template('form.html')

## Variable Rule
@app.route('/sucessif/<int:score>')
def sucess(score):
      
    return render_template('result1.html', results = score)

@app.route('/extra_marks/', methods = ['POST', "GET"])
def add_marks():
    marks = 10
    return redirect(url_for('/sucessif', score = marks))

if __name__ == '__main__':
    app.run(debug = True)
    