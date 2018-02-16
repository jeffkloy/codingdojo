from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

app.run(debug=True)