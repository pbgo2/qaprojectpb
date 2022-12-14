from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User,Players
from werkzeug.security import generate_password_hash,check_password_hash

from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)

# @auth.route('/login',methods=['GET','POST'])
# def login():
#     return render_template("login.html")

# @auth.route('/logout')
# def logout():
#     return "<p>Logout</p>"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        team = request.form.get('team')
        password = request.form.get('password')

        user = User.query.filter_by(team=team).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Team does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        team = request.form.get('team')
        country = request.form.get('country')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(team=team).first()
        if user:
            flash('Team already exists.', category='error')
        elif len(team) < 2:
            flash('Team must be greater than 1 characters.', category='error')
        elif len(country) < 2:
            flash('Country must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(team=team, country=country, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            # add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html",user=current_user)