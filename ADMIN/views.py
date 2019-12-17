from django.shortcuts import render
from USERS.models import Patient, Admin, Physician
from LAB.models import Test, Appointments
from LAB.forms import testForm
from USERS.views import createPhysician
from EQUIPMENT.models import Equipment
from COMPLAIN.models import Complaints
from NEWS_FEED.models import NewsFeed
from NEWS_FEED.forms import newsForm


def checkPatients(request):
    patients = Patient.objects.all()
    if patients:
        para = {'patients': patients}
        return render(request, '', para)
    else:
        message = 'No patients are registered yet'
        para = {'message': message}
        return render(request, '', para)


def checkDetails(request):
    admin = request.session['user']
    if admin:
        para = {'user': admin}
        return render(request, '', para)
    else:
        message = 'An error occurred please try again'
        para = {'message': message}
        return render(request, '', para)


def checkPhysicians(request):
    physicians = Physician.objects.all()
    if physicians:
        para = {'physicians': physicians}
        return render(request, '', para)
    else:
        message = 'No physicians registered yet'
        para = {'message': message}
        return render(request, '', para)


def checkTests(request):
    tests = Test.objects.all()
    if tests:
        para = {'tests': tests}
        return render(request, '', tests)
    else:
        message = "No tests registered yet"
        para = {'message': message}
        return render(request, '', para)


def addTest(request):
    if request.method == 'POST':
        form = testForm(request.POST)
        if form.is_valid():
            formObject = form.save()
            message = 'New Test Created Successfully'
            para = {'message': message, 'form': form}
            return render(request, '', para)
        else:
            message = "Invalid input please try again"
            para = {'message': message, 'form': form}
            return render(request, '', para)
    else:
        form = testForm()
        para = {'form': form}
        return render(request, '', para)


def editTest(request, pk):
    test = Test.objects.get(id=pk)
    if test:
        form = testForm(instance=test)
        if request.method == 'POST':
            filled_form = testForm(request.POST, instance=test)
            if filled_form.is_valid():
                filled_form.save()
                form = filled_form
                message = 'Test Updated Successfully'
                para = {'message': message, 'form': form}
                return render(request, '', para)
            else:
                message = 'Invalid Input'
                para = {'message': message}
                return render(request, '', para)
        else:
            para = {'form': form}
            return render(request, '', para)
    else:
        message = 'An error occurred while fetching data. Please retry'
        para = {'message': message}
        return render(request, '', para)


def checkAppointments(request):
    appointments = Appointments.objects.all()
    if appointments:
        para = {'appointments': appointments}
        return render(request, '', para)
    else:
        message = 'No appointments to show'
        para = {'message': message}
        return render(request, '', para)


def addPhysician(request):
    return createPhysician(request)


def checkEquipments(request):
    equipment = Equipment.objects.all()
    if equipment:
        para = {'equipments': equipment}
        return render(request, '', para)
    else:
        message = 'No new equipment required'
        para = {'message': message}
        return render(request, '', para)


def checkComplaints(request):
    complaints = Complaints.objects.all()
    if complaints:
        para = {'complaints': complaints}
        return render(request, '', para)
    else:
        messages = "No complaints to show yet"
        para = {'message': messages}
        return render(request, '', para)


def addNews(request):
    if request.methode == 'POST':
        form = newsForm(request.POST)
        if form.is_valid():
            news = form.save()
            message = 'News & Feed Aded Successfully'
            para = {'message': message, 'form': form}
            return render(request, '', para)
        else:
            message = 'Invalid Input'
            para = {'message': message, 'form': form}
            return render(request, '', para)
    else:
        form = newsForm()
        para = {'form': form}
        return render(request, '', para)


def updateNews(request, pk):
    news = NewsFeed.objects.get(id=pk)
    form = newsForm(instance=news)
    if request.method == 'POST':
        if news:
            filled_form = newsForm(request.POST, instance=news)
            if filled_form.is_valid():
                filled_form.save()
                form = filled_form
                message = 'Record Updated Successfully'
                para = {'form': form, 'message': message}
                return render(request, '', para)
            else:
                message = 'Invalid Input'
                para = {'form': form, 'message': message}
                return render(request, '', para)
        else:
            message = 'An error occurred. Please retry'
            para = {'form': form, 'message': message}
            return render(request, '', para)
    else:
        para = {'form': form}
        return render(request, '', para)
