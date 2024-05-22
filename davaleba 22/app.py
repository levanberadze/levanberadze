from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "python"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.form == "POST":
        user = request.form["username"]
        session['user'] = user
        return redirect(url_for('home'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('user', None)
    logout = "logged out"
    return render_template("login.html", text=logout)


if __name__ == "__main__":
    app.run(debug=True)
