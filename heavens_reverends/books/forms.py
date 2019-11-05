from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('HR Book Title', validators=[DataRequired()])
    author = StringField('HR Book Author', validators=[DataRequired()])
    book_content = TextAreaField('HR Book Content', validators=[DataRequired()])
    publish_date = DateTimeField('Publish Date', format='%m/%d/%y')
    submit = SubmitField('Publish')

# Could maybe combine this with above
class BookUpdateForm(FlaskForm):
    title = StringField('HR Post Title', validators=[DataRequired()])
    author = StringField('HR Book Author', validators=[DataRequired()])
    book_content = TextAreaField('HR Book Content', validators=[DataRequired()])
    publish_date = DateTimeField('Publish Date', format='%m/%d/%y')
    submit = SubmitField('Update')
    cancel = SubmitField('Cancel')
