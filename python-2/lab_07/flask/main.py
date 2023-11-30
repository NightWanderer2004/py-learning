# Postawić prosty serwis internetowy z wykorzystaniem Flask, bazując na QuickGuide ze strony https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        game = request.form['game']
        return render_template('game.html', game=game)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
