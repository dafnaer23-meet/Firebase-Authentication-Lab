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
  "databaseURL" : "https://login-b428a-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  email=request.form['email']
  password=request.form['password']
  username=request.form['username']
  full_name=request.form['full_name']
  bio=request.form["bio"]
  if request.method == 'GET':
    dict_user=db.child("Users").child(login_session['user']['localId']).set(dict_user)
    dict_user = {'email':'email','password':'password','full_name':'full_name','bio':'bio'}
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
  # create a dictionary called 'tweet' that has 3 key: 
  # title and text, the values are the inputs from the form
  tweet={"title":request.form["title"], "text":request.form["text"], "uid":login_session["user"]["localId"]}
  # uid: the value is the localId from the login_session
  # add "Tweets" child to database and push the new tweet (the new dictionary)
  db.child("tweets").push("tweet")
####### all of this can be found in the slides ###########
  return render_template("add_tweet.html")


@app.route('/all_tweets', methods=['GET', 'POST'])
def the_tweet():
  tweets = db.child("tweet").get().val()

#create a new route called all_tweets and an html page called "tweets.html"
# display the tweets with the child "Tweets" and with .get().val()


if __name__ == '__main__':
    app.run(debug=True)