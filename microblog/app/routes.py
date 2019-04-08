from flask import render_template, flash, redirect, url_for, request
from app import app, db 
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

'''This file serves as the "Home page route", which contains my first view function.'''

# from the app package, import the app variable that we made in our app package (the __init__.py file, which
# makes it a package.)


# The @app.route decorator (which modifies the function that follows it) creates an assocation between the URL 
# given as an argument and the function. 

#So, whenever the browser requests either URL ('/' or 'index'), then it will run the following function.
@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
                'author': {'username':'John'},
                'body': 'Beautiful day in Portland!'
        },
        {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
                return redirect(url_for('index'))
                
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first()
                if user is None or not user.check_password(form.password.data):
                        flash('Invalid username or password')
                        return redirect(url_for('login'))
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                        next_page = url_for('index')
                return redirect(next_page)
        return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
                user = User(username=form.username.data, email=form.email.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                flash('Congratulations, you are now a registered user!')
                return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)