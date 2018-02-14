from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase="Hello world!", times=5)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/success')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html', username=username)

app.run(debug=True)