from flask import render_template, request, Blueprint
from heavens_reverends.models import Post, Book

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page,per_page=5)

    return render_template('index.html', posts=posts)

@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/books')
def books():
    page = request.args.get('page',1,type=int)
    books = Book.query.order_by(Book.publish_date.desc()).paginate(page=page,per_page=5)

    return render_template('books.html', books=books)
