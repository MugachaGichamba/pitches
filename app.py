from flask import Flask, render_template

app = Flask(__name__)

pitches = [
    {
        'author': 'Mugacha Gichamba',
        'category': "wordplay",
        'pitch': "mkinunua loaf haiko sliced lazima mkate",
        "likes": 3,
        "dislikes": 0,
        "comments": ["fiti", "kijana round"],
        "date posted": "April 23rd 2019"

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'about!'


if __name__ == '__main__':
    app.run()
