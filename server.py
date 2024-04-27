from flask import Flask, render_template, jsonify, request,session,url_for
import json
from datetime import datetime
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
correct_answers = qim['correct_answers']

user_page_enter_times = {
    'welcome' : [],
    'introduction_chart' : [],
    'introduction_trade' : [],
    'quiz_0' : [],
    'quiz_1' : [],
    'quiz_2' : [],
    'quiz_3' : [],
    'quiz_score' : [],
    'the_basics' : []
}
for i in range(1, 13):
    user_page_enter_times[f'learn_{i}'] = []

# ROUTES
@app.route('/')
def welcome():
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times['welcome'].append(access_time)
    return render_template('welcome.html', data={})

@app.route('/learn/<int:id>')
def learn(id):
    lesson = lessons[str(id)]  # This line fetches the current lesson
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times[f'learn_{id}'].append(access_time)
    return render_template('learn.html', id=id, lesson=lesson, lessons=lessons)  # Pass `lessons` to the template

@app.route('/introduction_chart')
def introduction_chart():
    page = chart
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times['introduction_chart'].append(access_time)
    return render_template('introduction.html', page=page)

@app.route('/introduction_trade')
def introduction_trade():
    page = trade
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times['introduction_trade'].append(access_time)
    return render_template('introduction.html', page=page)

@app.route('/quiz/<int:id>')
def quiz(id):
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times[f'quiz_{id}'].append(access_time)
    return render_template('quiz.html', id=id, data=qim)


@app.route('/learn/0')
def the_basics():
    acccess_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times['the_basics'].append(acccess_time)
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
                    incorrect_questions.append((key, correct_answer, get_image_url(key), get_question_url(key)))
            else:
                if user_answer == correct_answer:
                    score += 1
                else:
                    incorrect_questions.append((key, correct_answer, get_image_url(key), get_question_url(key)))

    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_page_enter_times['quiz_score'].append(access_time)
    return render_template('score.html', score=score, incorrect_questions=incorrect_questions)

def get_image_url(question_key):
    # Define a mapping of question keys to image URLs
    image_urls = {
        'question1': 'https://i.ibb.co/cc3BmpY/p1.png',
        'question2': 'https://i.ibb.co/zssdf5T/p2.png',
        'question3': 'https://i.ibb.co/3mKtYFw/p3.png',
        'drop1': 'https://i.ibb.co/x3Z2ZzM/WX20240423-222011-2x.png',
        'drop2': 'https://i.ibb.co/Qk6RcQs/WX20240423-222027-2x.png',
        'image6': 'https://i.ibb.co/Mkpg6Dr/Screenshot-2024-04-16-at-4-39-05-PM.png',
        'image7': 'https://i.ibb.co/9npczgc/Screenshot-2024-04-16-at-4-39-11-PM.png'
    }
    return image_urls.get(question_key, '')

def get_question_url(question_key):
    # Define a mapping of question keys to question page URLs
    question_urls = {
        'question1': url_for('quiz', id=1),
        'question2': url_for('quiz', id=1),
        'question3': url_for('quiz', id=1),
        'drop1': url_for('quiz', id=2),
        'drop2': url_for('quiz', id=2),
        'image6': url_for('quiz', id=3),
        'image7': url_for('quiz', id=3)
    }
    return question_urls.get(question_key, '')

if __name__ == '__main__':
    app.run(debug=True)





