from flask import Flask, render_template, url_for, request, redirect, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "jasurbeki"
app.permanent_session_lifetime = timedelta(days=5)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session['user'] = user
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    logout = "you are logged out"
    return render_template('index.html', text=logout)









if __name__ == "__main__":
    app.run(debug=True)
