import random
from flask import *

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/', methods=['GET'])
def index():
    session['number'] = 50 ##random.randint(0, 101)
    if session['guess'] == session['number']:
        print "User entered: " + session['guess'] + ", so user is right!"
        print str(session['number']) + " was the answer."
        return render_template('success.html', number=session['number'], guess=session['guess'])
    elif session['guess'] != session['number']:
        print "User entered: " + session['guess'] + ", so user is wrong!"
        print str(session['number']) + " was the answer."
        return render_template('index.html', number=session['number'], guess=session['guess'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    return redirect('/')

app.run(debug=True)
