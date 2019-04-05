from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm
'''This file serves as the "Home page route", which contains my first view function.'''

# from the app package, import the app variable that we made in our app package (the __init__.py file, which
# makes it a package.)


# The @app.route decorator (which modifies the function that follows it) creates an assocation between the URL 
# given as an argument and the function. 

#So, whenever the browser requests either URL ('/' or 'index'), then it will run the following function.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                flash('Login requested for user {}, remember_me={}'.format(
                        form.username.data, form.remember_me.data))
                return redirect(url_for('/index')) 
        return render_template('login.html', title='Sign In', form=form)