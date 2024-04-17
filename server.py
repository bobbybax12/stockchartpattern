from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load JSON data from qim.json
with open('static/qim.json') as f:
    qim = json.load(f)

chart = qim['9']
trade = qim['10']
lessons = qim['lessons']
quiz_results = []
correct_answers = {
    'question0': 'Triangle',
    'question1': 'Head & Shoulders',
    'question2': 'Cup & Handle',
    'drop1': ['Head & Shoulders', 'Cup & Handle'],
    'drop2': ['Descending Triangle', 'Reverse Pennant'],
    'image6': 'buy',
    'image7': 'sell'
}
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


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    quiz_data = request.json

    score = 0
    for key in quiz_data:
        user_answer = quiz_data[key]
        correct_answer = correct_answers[key]
        if isinstance(correct_answer, list):
            if set(user_answer) == set(correct_answer):
                score += 1
        else:
            if user_answer == correct_answer:
                score += 1

    quiz_data['score'] = score  # Add the 'score' key to the quiz_data dictionary
    quiz_results.append(quiz_data)

    return jsonify({'message': 'Quiz submitted successfully', 'score': score})

@app.route('/learn/0')
def the_basics():
    return render_template('the_basics.html')

@app.route('/quiz/score')
def quiz_score():
    score = quiz_results[-1]['score']  # Retrieve the score from the last submitted quiz
    return render_template('score.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)





