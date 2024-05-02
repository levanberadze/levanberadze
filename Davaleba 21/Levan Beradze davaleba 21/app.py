from flask import Flask, render_template, request, url_for, redirect
app: Flask = Flask(__name__)


books = [
    {"id": 1, "title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "year": 1866},
    {"id": 2, "title": "The Great Gatsby", "Author": " F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "year": 1880},
    {"id": 4, "title": "To Kill a Mockingbird", "Author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "The Lord of the Rings", "Author": "John Ronald Reuel Tolkien", "year": 1954},
]


@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = books.pop(book_id)
    if book:
        return render_template("book.html", book=books[book_id])
    else:
        return "ar aris"


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        book_id = len(books) + 1
        return redirect(url_for('index'))
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
