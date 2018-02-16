from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'cd4f5e2a8c458a44c0683f8b22304c8675fb9ee6f2e5675c38417ad2f4252b45'

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
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html', username=username)

@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])

app.run(debug=True)
