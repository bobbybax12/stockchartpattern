from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

data = {}
# ROUTES
@app.route('/')
def welcome():
   return render_template('welcome.html', data=data)

@app.route('/learn/<id>')
def learn(id):
   return render_template('learn.html', id=id)

@app.route('/quiz/<id>')
def quiz(id):
   return render_template('quiz.html', id=id)

if __name__ == '__main__':
   app.run(debug = True)




