from flask import render_template, url_for, flash, redirect
from App.__init__ import app, db, bcrypt
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
    if current_user .is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('Login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('Login.html', title='Login', form=form)