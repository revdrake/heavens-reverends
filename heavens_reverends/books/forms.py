from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms_components.fields.html5 import DateField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('HR Book Title', validators=[DataRequired()])
    author = StringField('HR Book Author', validators=[DataRequired()])
    book_content = TextAreaField('HR Book Content', validators=[DataRequired()])
    publish_date = DateField('Publish Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Publish')

# Could maybe combine this with above
class BookUpdateForm(FlaskForm):
    title = StringField('HR Post Title', validators=[DataRequired()])
    author = StringField('HR Book Author', validators=[DataRequired()])
    book_content = TextAreaField('HR Book Content', validators=[DataRequired()])
    publish_date = DateField('Publish Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Update')
    cancel = SubmitField('Cancel')
