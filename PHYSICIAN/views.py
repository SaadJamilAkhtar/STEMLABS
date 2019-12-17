from django.shortcuts import render, redirect
from USERS.models import Patient
from LAB.models import Appointments
from .forms import updateProgressForm
from NEWS_FEED.models import NewsFeed
from COMPLAIN.forms import complaintForm
from COMPLAIN.models import Complaints
from EQUIPMENT.models import Equipment
from EQUIPMENT.forms import EquipmentEdit


def checkDetails(request):
    physician = request.session['user']
    if physician:
        para = {'user': physician}
        return render(request, '', para)
    else:
        message = 'An error occurred please try again'
        para = {'message': message}
        return render(request, '', para)


def checkPatients(request):
    patients = Patient.objects.all()
    if patients:
        para = {'patients': patients}
        return render(request, '', para)
    else:
        message = 'No patients to show'
        para = {'message': message}
        return render(request, '', para)


def checkAppointments(request):
    appointments = Appointments.objects.all().reverse()
    if appointments:
        try:
            message = request.session['message']
            request.session['message'] = None
            para = {'appointments': appointments, 'message': message}
        except:
            para = {'appointments': appointments}
        return render(request, 'USERS/checkAppointments.html', para)
    else:
        message = 'No appointments to show'
        para = {'message': message}
        return render(request, 'USERS/checkAppointments.html', para)


def updateProgress(request, appointmentId):
    appointment = Appointments.objects.get(id=appointmentId)
    if appointment:
        if request.method == 'POST':
            form = updateProgressForm(request.POST, request.FILES, instance=appointment)
            if form.is_valid():
                form.save()
                message = 'Appointment updated successfully'
                request.session['message'] = message
                return redirect('../showAppointments')
            else:
                message = 'Invalid Input'
                para = {'message': message, 'form': form}
                return render(request, 'USERS/editAppointment.html', para)
        else:
            form = updateProgressForm()
            para = {'form': form}
            return render(request, 'USERS/editAppointment.html', para)
    else:
        message = 'An error occurred. Please retry'
        para = {'message': message}
        return render(request, 'USERS/editAppointment.html', para)


def physicianNews(request):
    news = NewsFeed.objects.all()
    news = news.reverse()
    if news:
        latest = news[:3]
        para = {'news': news, 'latest': latest}
        return render(request, 'USERS/physicianNews.html', para)
    else:
        message = 'No news added yet'
        para = {'message': message}
        return render(request, 'USERS/physicianNews.html', para)


def checkEquipments(request):
    equipments = Equipment.objects.all()
    if equipments:
        try:
            message = request.session['message']
            request.session['message'] = None
            para = {'equipments': equipments, 'message': message}
        except:
            para = {'equipments': equipments}
        return render(request, 'USERS/equipment.html', para)
    else:
        message = 'No equipment added yet'
        para = {'message': message}
        return render(request, 'USERS/equipment.html', para)


def editEquipment(request, equipmentId):
    equipment = Equipment.objects.get(id=equipmentId)
    if request.method == "POST":
        form = EquipmentEdit(request.POST)
        if form.is_valid():
            equipment.quantity = form.cleaned_data['quantity']
            equipment.save()
            message = 'Equipment Updated Successfuly'
            request.session['message'] = message
            return redirect('../checkEquipment')
        else:
            message = 'Invalid Input'
            request.session['message'] = message
            return redirect('../checkEquipment')
    form = EquipmentEdit()
    para = {'form': form}
    return render(request, 'USERS/editEquipment.html', para)
