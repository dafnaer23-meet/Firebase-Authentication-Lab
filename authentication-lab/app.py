from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



firebaseConfig = {

  "apiKey": "AIzaSyCcVltzXngMxbS2Yufb-R-Nov6ry5uBzf8",

  "authDomain": "login-b428a.firebaseapp.com",

  "projectId": "login-b428a",

  "storageBucket": "login-b428a.appspot.com",

  "messagingSenderId": "653591106935",

  "appId": "1:653591106935:web:5f88b914822571aa6e7d72",

  "measurementId": "G-C89LKJP4T7",
  "databaseURL" : ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
    login_session['email'] = request.form['email']
    login_session['password'] = request.form['password']
    email = login_session['email']
    password = login_session['password'] 
    
    try:
      login_session['user'] = auth.create_user_with_email_and_password(login_session['email'], login_session['password'])
      return redirect(url_for('add_tweet'))
    except:
      error = "Authentication failed"
      return error

def signup():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    login_session['email'] = request.form['email']
    login_session['password'] = request.form['password']
    email = login_session['email']
    password = login_session['password'] 
    
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(login_session['email'], login_session['password'])
      return redirect(url_for('add_tweet'))
    except:
      error = "Authentication failed"
      return error


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)