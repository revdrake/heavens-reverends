from flask import render_template,url_for,flash,request,redirect,Blueprint,abort
from flask_login import current_user,login_required
from heavens_reverends import db
from heavens_reverends.models import Appointment
from heavens_reverends.appointments.forms import (AppointmentForm, AppointmentUpdateForm, WeddingAppointmentForm, WeddingAppointmentUpdateForm,
                                                 CustomizeWeddingForm)
from datetime import datetime, timedelta

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
    appointment_type = 'wedding'

    if form.validate_on_submit():
        appointment = Appointment(
                        appointment_type=appointment_type,
                        appointment_date=form.appointment_date.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        spouse_first_name=form.spouse_first_name.data,
                        spouse_last_name=form.spouse_last_name.data,
                        user_id=current_user.id)
        db.session.add(appointment)
        db.session.commit()
        flash('Wedding Appointment Booked!')
        return redirect(url_for('appointments.user_appointments'))


    return render_template('book_wedding_appointment.html',form=form)

# READ
@appointments.route('/appointments/myappointments',methods=['GET','POST'])
@login_required
def user_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id)
    return render_template('user_appointments.html',appointments=appointments)

# UPDATE
@appointments.route('/appointments/myappointments/<int:appointment_id>/update',methods=['GET','POST'])
@login_required
def update_wedding_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    if appointment.user_id != current_user.id:
        abort(403)

    form = WeddingAppointmentUpdateForm()

    if form.validate_on_submit():
        appointment.first_name = form.first_name.data
        appointment.last_name = form.last_name.data
        appointment.spouse_first_name = form.spouse_first_name.data
        appointment.spouse_last_name = form.spouse_last_name.data
        appointment.appointment_date = form.appointment_date.data
        appointment.appointment_type = 'wedding'
        db.session.commit()
        flash('Appointment Updated')
        return redirect(url_for('appointments.user_appointments'))

    elif request.method == 'GET':
        form.first_name.data = appointment.first_name
        form.last_name.data = appointment.last_name
        form.spouse_first_name.data = appointment.spouse_first_name
        form.spouse_last_name.data = appointment.spouse_last_name
        form.appointment_date.data = appointment.appointment_date

    return render_template('book_wedding_appointment.html',title='Updating',form=form)


@appointments.route('/appointments/myappointments/<int:appointment_id>/customize',methods=['GET','POST'])
@login_required
def customize_wedding(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    if appointment.user_id != current_user.id:
        abort(403)

    form = CustomizeWeddingForm()
    if form.validate_on_submit():
        has_update_data = (appointment.theme != form.theme.data \
                              or appointment.length_minutes != form.length_minutes.data) \
                              or appointment.religious_verses != form.religious_verses.data \
                          and (form.theme.data is not None
                              or form.length_minutes.data is not None
                              or form.religious_verses.data is not None)
        if has_update_data:
            appointment.theme = form.theme.data
            appointment.length_minutes = form.length_minutes.data
            appointment.religious_verses = form.religious_verses.data
            db.session.commit()
            flash('Wedding Customized!')
        return redirect(url_for('appointments.user_appointments'))
    elif request.method == 'GET':
        form.theme.data = appointment.theme
        form.length_minutes.data = appointment.length_minutes
        form.religious_verses.data = appointment.religious_verses


    return render_template('customize_wedding.html',title='Customize Wedding',form=form)



#DELETE
@appointments.route('/appointments/myappointments/<int:appointment_id>/delete',methods=['GET','POST'])
@login_required
def delete_wedding_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    if appointment.user_id != current_user.id:
        abort(403)

    db.session.delete(appointment)
    db.session.commit()
    flash('Appointment Deleted')
    return redirect(url_for('appointments.user_appointments'))
