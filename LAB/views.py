from django.shortcuts import render, redirect
from .models import Appointments, Test
from .forms import *
from USERS.models import Patient
from PATIENT.views import checkTests


def makeAppointment(request, testId):
    patient = Patient.objects.get(id=request.session['user'])
    test = Test.objects.get(id=testId)
    appointment = Appointments(patient_id=patient, test_id=test)
    appointment.save()
    message_ = 'APPOINTMENT ADDED SUCCESSFULLY'
    request.session['message'] = message_
    return redirect('../services')
