from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page"

@app.route('/about')
def about():
    return "This is about page"

@app.route('/third')
def third():
    return "This is third page"

if __name__ == '__main__':
    app.run(debug=True)