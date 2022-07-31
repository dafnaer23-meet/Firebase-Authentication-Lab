from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  apiKey: "AIzaSyBSqeUlc81M5UGbfSLWnCH1pxSiHPjp9Qw",
  authDomain: "bjhbjhb-63bfd.firebaseapp.com",
  projectId: "bjhbjhb-63bfd",
  storageBucket: "bjhbjhb-63bfd.appspot.com",
  messagingSenderId: "985216799062",
  appId: "1:985216799062:web:b62627a0d0a67a1f0806f7",
  measurementId: "G-N4B71HJVBH"
}



@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)