from flask import render_template, url_for, flash, redirect
from App.__init__ import app
from App.forms import RegistrationForm, LoginForm
from App.models import User, Pitch


pitches = [
    {
        'author': 'Alexander oke',
        'title': 'pitch 1',
        'content': 'First post content',
        'date_posted': 'Febuary 10, 2022',
    },
    {
        'author': 'Alex William',
        'title': 'pitch 2',
        'content': 'Second post content',
        'date_posted': 'Febuary 10, 2022',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pitch.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)