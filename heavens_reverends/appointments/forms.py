from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms_components import TimeField
from wtforms_components.fields.html5 import DateTimeLocalField, DateTimeField
from wtforms.validators import DataRequired, Optional
# from wtforms_components.widgets import DateTimeInput

class AppointmentForm(FlaskForm):
    appointment_type = SelectField(label='Appointment Type',choices=['Wedding Ceremony','Something Else'], validators=[DataRequired()])
    submit = SubmitField('Go')

class WeddingAppointmentForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    spouse_first_name = StringField('Spouse First Name', validators=[DataRequired()])
    spouse_last_name = StringField('Spouse Last Name', validators=[DataRequired()])
    appointment_date = DateTimeLocalField('Appointment Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book')

# Could maybe combine this with above
class AppointmentUpdateForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    appointment_type = TextAreaField('Appointment Type', validators=[DataRequired()])
    appointment_date = DateTimeField('Appointment Date', format='%m/%d/%y')
    submit = SubmitField('Update')
    cancel = SubmitField('Cancel')

class WeddingAppointmentUpdateForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    spouse_first_name = StringField('Spouse First Name', validators=[DataRequired()])
    spouse_last_name = StringField('Spouse Last Name', validators=[DataRequired()])
    appointment_date = DateTimeLocalField('Appointment Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField(label='Update')

class CustomizeWeddingForm(FlaskForm):
    theme = StringField('Theme',validators=[]) # ,validators=[DataRequired()])
    # hours = IntegerField()
    length_minutes = IntegerField('Time (Minutes)',validators=[Optional()])
    religious_verses = StringField('Religious Verses',validators=[Optional()])
    # attire
    # dual_reverend
    submit = SubmitField('Submit')
