# blog_posts/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from heavens_reverends import db
from heavens_reverends.models import Book
from heavens_reverends.books.forms import BookForm, BookUpdateForm

books = Blueprint('books',__name__)

# CREATE
@books.route('/write',methods=['GET','POST'])
@login_required
def add_book():
    form = BookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data,
                    author=form.author.data,
                    content=form.book_content.data,
                    publish_date=form.publish_date.data
                    )
        db.session.add(book)
        db.session.commit()
        flash('Book Added')
        return redirect(url_for('core.books'))

    return render_template('add_book.html',form=form)
# READ
@books.route('/books/<int:book_id>')
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html',title=book.title,
                                       author=book.author,
                                       contents=book.content,
                                       publish_date=book.publish_date,
                                       book=book)

# UPDATE
@books.route('/<int:book_id>/update',methods=['GET','POST'])
@login_required
def update_book(post_id):
    book = Book.query.get_or_404(post_id)
    if book.author != current_user:
        abort(403)

    form = BookUpdateForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.autor.data
        if form.submit.data:
            db.session.commit()
            flash('Book Updated')
        return redirect(url_for('books.book',book_id=book.id))
    elif request.method == 'GET':
        form.title.data = book.title
        form.contents.data = book.content

    return render_template('update_book.html',title='Updating',form=form)

#DELETE
@books.route('/<int:book_id>/delete',methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Book Deleted')
    return redirect(url_for('core.index'))
