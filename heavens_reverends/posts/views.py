# blog_posts/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint,abort
from flask_login import current_user,login_required
from heavens_reverends import db
from heavens_reverends.models import Post
from heavens_reverends.posts.forms import PostForm, PostUpdateForm

posts = Blueprint('posts',__name__)

# CREATE
@posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    text=form.text.data,
                    user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html',form=form)
# READ
@posts.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title
                          ,created_at=post.created_at,post=post)

# UPDATE
@posts.route('/<int:post_id>/update',methods=['GET','POST'])
@login_required
def update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    form = PostUpdateForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        if form.submit.data:
            db.session.commit()
            flash('Post Updated')
        return redirect(url_for('posts.post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text

    return render_template('create_post.html',title='Updating',form=form)

#DELETE
@posts.route('/<int:post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted')
    return redirect(url_for('core.index'))
