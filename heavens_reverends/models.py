from heavens_reverends import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='hr_logo.jpg')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'Username: {self.username}'

class Post(db.Model):

    __tablename__ = 'posts'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'Post ID: {self.id} -- Created At {self.created_at} -- Title: {self.title}'


class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    publish_date = db.Column(db.DateTime)

    def __init__(self, title, author, content, publish_date):
        self.title = title
        self.author = author
        self.content = content
        self.publish_date = publish_date

    def __repr__(self):
        return f"{self.title} by {self.author} Published: {self.publish_date}"


class Appointment(db.Model):

    __tablename__ = 'appointments'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    appointment_type = db.Column(db.Text, nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False, default=datetime(9999,12,31)) # False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    spouse_first_name = db.Column(db.Text, nullable=False)
    spouse_last_name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
