from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data from qim.json
with open('static/qim.json') as f:
    qim = json.load(f)

chart = qim['9']
trade = qim['10']
lessons = qim['lessons']

# ROUTES
@app.route('/')
def welcome():
    return render_template('welcome.html', data={})

@app.route('/learn/<int:id>')
def learn(id):
    lesson = lessons[str(id)]
    return render_template('learn.html', id=id, lesson=lesson, data=qim)

@app.route('/introduction_chart')
def introduction_chart():
    page = chart
    return render_template('introduction.html', page=page)

@app.route('/introduction_trade')
def introduction_trade():
    page = trade
    return render_template('introduction.html', page=page)

@app.route('/quiz/<int:id>')
def quiz(id):
    return render_template('quiz.html', id=id, data=qim)

@app.route('/learn/0')
def the_basics():
    return render_template('the_basics.html')

if __name__ == '__main__':
    app.run(debug=True)





