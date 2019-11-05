from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('HR Post Title', validators=[DataRequired()])
    text = TextAreaField('HR Post Text', validators=[DataRequired()])
    submit = SubmitField = SubmitField('Post')

# Could maybe combine this with above
class PostUpdateForm(FlaskForm):
    title = StringField('HR Post Title', validators=[DataRequired()])
    text = TextAreaField('HR Post Text', validators=[DataRequired()])
    submit = SubmitField('Update')
    cancel = SubmitField('Cancel')
