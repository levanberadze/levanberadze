from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

# Mock user data
class User:
    def __init__(self, id):
        self.id = id
        self.username = f"user{id}"
        self.password = f"password{id}"
        self.is_admin = (id == 1)  # Simulate admin user

# Mock database of users
users = {1: User(1), 2: User(2)}

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((user for user in users.values() if user.username == username and user.password == password), None)
        if user:
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Protected route that requires authentication
@app.route('/')
def index():
    # Simulate user authentication
    user_id = request.args.get('user_id')
    if user_id:
        user = users.get(int(user_id))
        if user:
            return f'Hello, {user.username}!'
    return redirect(url_for('login'))

# About Us page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

