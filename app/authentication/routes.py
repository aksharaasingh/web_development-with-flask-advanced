from flask import render_template,request,flash,redirect,url_for
from app.authentication.forms import RegistrationForm
from app.authentication import authentication as at
from app.authentication.models import User

@at.route('/register',methods = ['GET','POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(user = form.name.data,
                         email = form.email.data,
                         password = form.password.data )
        flash("Registration Successful!!!")
        return redirect (url_for(at.login_user) )
    return render_template('registration.html',form = form)


@at.route('/login',methods = ['GET','POST'])
def login_user():
    return render_template('login.html')