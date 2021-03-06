from app import app
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm

from flask_login import current_user, login_user , logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse 

mock_user = {"username" : "Evgen", 'phone' : '+9 999 222 333 444'}
mock_posts = [
    {
        'author' : {"username" : "Bob"},
        'body' : "It's my first post on this site!",
    },
    {
        'author' : {"username" : "Alice"},
        'body' : "Cool!",
    },
    {
        'author' : {"username" : "Alex"},
        'body' : "My fav book is LOTR!",
    },
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', title= 'Home', posts=mock_posts)


@app.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('about.html', user=mock_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash('Invalid username. Try login again')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Invalid password. Try login again')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('about')
            return redirect(next_page)

    return render_template('login.html', form=form )


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))




