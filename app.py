from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f04d4ad95aa5cb663854acb929d69a01'

pitches = [
    {
        'author': 'Mugacha Gichamba',
        'category': "wordplay",
        'pitch': "mkinunua loaf haiko sliced lazima mkate",
        "likes": 3,
        "dislikes": 0,
        "comments": ["fiti", "kijana round"],
        "date_posted": "April 23rd 2019"

    },
    {
        'author': 'Nicollo Machiavelli',
        'category': "quotes",
        'pitch': "In my view",
        "likes": 5,
        "dislikes": 4,
        "comments": ["fiti", "kijana round"],
        "date_posted": "April 23rd 2019"

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pitches=pitches, title="Home")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Created your account: {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run()
