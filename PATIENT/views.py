from django.shortcuts import render
from LAB.models import Test, Appointments
from COMPLAIN.forms import complaintForm
from COMPLAIN.models import Complaints
from USERS.models import Patient


def checkDetails(request):
    patient = Patient.objects.get(id=request.session['user'])
    if patient:
        para = {'user': patient}
        return render(request, '', para)
    else:
        message = 'An error occurred please try again'
        para = {'message': message}
        return render(request, '', para)


def checkTests(request):
    tests = Test.objects.all()
    if tests:
        try:
            message = request.session['message']
            request.session['message'] = None
            para = {'tests': tests, 'message': message}
            return render(request, 'USERS/services.html', para)
        except:
            para = {'tests': tests}
            return render(request, 'USERS/services.html', para)

    else:
        message = "No tests registered yet"
        para = {'message': message}
        return render(request, 'USERS/services.html', para)


def checkProgress(request):
    tests = Appointments.objects.filter(patient_id=int(request.session['user']))
    if tests:
        para = {'tests': tests}
        return render(request, 'USERS/history.html', para)
    else:
        message = 'No Appointments added yet'
        para = {'message': message}
        return render(request, 'USERS/history.html', para)


def addComplaint(request):
    if request.method == 'POST':
        form = complaintForm(request.POST)
        if form.is_valid():
            complaint = Complaints(title=form.cleaned_data['title'], description=form.cleaned_data['description'],
                                   patient_id=request.session['user'].id)
            complaint.save()
            message = 'Complaint registered successfully'
            para = {'form': form, 'message': message}
            return render(request, '', para)
        else:
            message = 'Incorrect Input'
            para = {'message': message, 'form': form}
            return render(request, '', para)
    else:
        form = complaintForm()
        para = {'form': form}
        return render(request, '', para)
