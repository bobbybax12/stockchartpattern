from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data from qim.json
with open('static/qim.json') as f:
    qim = json.load(f)

# Dummy lessons data
lessons = {
    1: {"title": "Cup and Handle Pattern", "description": "Learn the basics of trading.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Cup-and-Handle.jpg"},
    2: {"title": "The Pennant Pattern", "description": "Understand how to analyze market trends.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Pennant.jpg"},
    3: {"title": "Head and Shoulders Pattern", "description": "Explore the fundamentals of technical analysis.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Head-and-Shoulders.jpg"},
    4: {"title": "Triangle Pattern", "description": "Learn about risk management techniques.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=706/https://content.stockstotrade.com/wp-content/uploads/2022/02/Triangle.jpg"},
    5: {"title": "Flag Pattern", "description": "Create a personalized trading plan.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Flag.jpg"},
    6: {"title": "Gaps", "description": "Create a personalized trading plan.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=574/https://content.stockstotrade.com/wp-content/uploads/2022/02/Gaps.jpg"},
    7: {"title": "Cup and Handle Pattern", "description": "Learn the basics of trading.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Cup-and-Handle.jpg"},
    8: {"title": "The Pennant Pattern", "description": "Understand how to analyze market trends.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Pennant.jpg"},
    9: {"title": "Head and Shoulders Pattern", "description": "Explore the fundamentals of technical analysis.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Head-and-Shoulders.jpg"},
    10: {"title": "Triangle Pattern", "description": "Learn about risk management techniques.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=706/https://content.stockstotrade.com/wp-content/uploads/2022/02/Triangle.jpg"},
    11: {"title": "Flag Pattern", "description": "Create a personalized trading plan.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=870/https://content.stockstotrade.com/wp-content/uploads/2022/02/Flag.jpg"},
    12: {"title": "Gaps", "description": "Create a personalized trading plan.", "image": "https://content.stockstotrade.com/cdn-cgi/image/quality=100,format=webp,width=574/https://content.stockstotrade.com/wp-content/uploads/2022/02/Gaps.jpg"},
}
introduction_chart = {
    "title": "Essential Chart Patterns",
    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.",
    "image": "https://www.bankrate.com/2019/03/22142110/How-to-trade-stocks.jpg"
}

introduction_trade = {
    "title": "How to Trade These Patterns",
    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.",
    "image": "https://www.bankrate.com/2019/03/22142110/How-to-trade-stocks.jpg"
}

# ROUTES
@app.route('/')
def welcome():
    return render_template('welcome.html', data={})

@app.route('/learn/<int:id>')
def learn(id):
    lesson = lessons.get(id)
    return render_template('learn.html', id=id, lesson=lesson, data=qim)

@app.route('/introduction_chart')
def introduction_chart():
    return render_template('introduction_chart.html', page=introduction_chart)

@app.route('/introduction_trade')
def introduction_trade():
    return render_template('introduction_trade.html', page=introduction_trade)


@app.route('/quiz/<int:id>')
def quiz(id):
    return render_template('quiz.html', id=id, data=qim.get(id, {}))

@app.route('/learn/0')
def the_basics():
    return render_template('the_basics.html')

if __name__ == '__main__':
    app.run(debug=True)





