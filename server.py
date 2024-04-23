from flask import Flask, render_template, jsonify, request,session
import json
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key
# Load JSON data from qim.json
with open('static/qim.json') as f:
    qim = json.load(f)

chart = qim['9']
trade = qim['10']
lessons = qim['lessons']
quiz_results = []
question_map= qim['question_map']
# ROUTES
@app.route('/')
def welcome():
    return render_template('welcome.html', data={})

@app.route('/learn/<int:id>')
def learn(id):
    lesson = lessons[str(id)]  # This line fetches the current lesson
    return render_template('learn.html', id=id, lesson=lesson, lessons=lessons)  # Pass `lessons` to the template

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

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    quiz_data = request.json
    if 'user_answers' not in session:
        session['user_answers'] = {}
    # Store the user's answers in the session
    session['user_answers'].update(quiz_data)
    session.modified = True  # Notify Flask that the session has been modified
    return jsonify({'message': 'Quiz submitted successfully'})


@app.route('/quiz/score')
def quiz_score():
    user_answers = session.get('user_answers')
    print(user_answers)
    correct_answers = {
        # Define the correct answers for each question
        'question1': 'Triangle',
        'question2': 'Head & Shoulders',
        'question3': 'Cup & Handle',
        'drop1': ['Head & Shoulders', 'Cup & Handle'],
        'drop2': ['Descending Triangle', 'Reverse Pennant'],
        'image6': 'buy',
        'image7': 'sell'
    }

    score = 0
    incorrect_questions = []
    for key in user_answers:
        user_answer = user_answers[key]
        correct_answer = correct_answers.get(key)
        if correct_answer is not None:
            if isinstance(correct_answer, list):
                if set(user_answer) == set(correct_answer):
                    score += 1
                else:
                    incorrect_questions.append(key)
            else:
                if user_answer == correct_answer:
                    score += 1
                else:
                    incorrect_questions.append(key)

    return render_template('score.html', score=score, incorrect_questions=incorrect_questions, question_map=question_map)
if __name__ == '__main__':
    app.run(debug=True)





