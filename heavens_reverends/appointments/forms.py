from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField, SelectField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    appointment_type = SelectField(label='Appointment Type',choices=['Wedding Ceremony','Something Else'], validators=[DataRequired()])
    submit = SubmitField('Go')

class WeddingAppointmentForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    spouse_first_name = StringField('Spouse First Name', validators=[DataRequired()])
    spouse_last_name = StringField('Spouse Last Name', validators=[DataRequired()])
    appointment_date = DateTimeField('Appointment Date', format='%m/%d/%y', validators=[DataRequired()])
    submit = SubmitField('Book')

# Could maybe combine this with above
class AppointmentUpdateForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    appointment_type = TextAreaField('Appointment Type', validators=[DataRequired()])
    appointment_date = DateTimeField('Appointment Date', format='%m/%d/%y')
    submit = SubmitField('Update')
    cancel = SubmitField('Cancel')
