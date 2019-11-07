# blog_posts/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from heavens_reverends import db
from heavens_reverends.models import Appointment
from heavens_reverends.appointments.forms import AppointmentForm, AppointmentUpdateForm, WeddingAppointmentForm
from datetime import datetime

appointments = Blueprint('appointments',__name__)

@appointments.route('/appointments', methods=['GET','POST'])
@login_required
def book_appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        appointment_type = form.appointment_type.data
        session['appointment_type'] = appointment_type
        return redirect(url_for('book_'+appointment_type+'_appointment'))

    return render_template('appointments.html', form=form)



# CREATE
@appointments.route('/appointments/wedding',methods=['GET','POST'])
@login_required
def book_wedding_appointment():
    form = WeddingAppointmentForm()
    appointment_type = 'wedding' # session.get('appointment_type', None)

    if form.validate_on_submit():
        year = form.year.data
        month = form.month.data
        day = form.day.data
        hour = form.hour.data
        appointment_date = datetime(year,month,day,hour)
        appointment = Appointment(
                        appointment_type=appointment_type,
                        appointment_date=appointment_date,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        spouse_first_name=form.spouse_first_name.data,
                        spouse_last_name=form.spouse_last_name.data,
                        user_id=current_user.id)
        db.session.add(appointment)
        db.session.commit()
        flash('Wedding Appointment Booked!')
        return redirect(url_for('core.index'))

    return render_template('book_wedding_appointment.html',form=form)

# READ
@appointments.route('/appointments/myappointments',methods=['GET','POST'])
@login_required
def user_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id)
    return render_template('user_appointments.html',appointments=appointments)
