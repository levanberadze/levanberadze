from flask import Flask, render_template

web = Flask(__name__)

@web.route('/')
def home():
    return 'This is a home page'


@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/resume')
def resume():
    return render_template('resume.html')



if __name__ == '__main__':
    web.run(debug=True)



