from django.shortcuts import render
from .models import Complaints, physicianComplaints
from .forms import complaintForm, physicianComplaintForm
from USERS.models import Patient, Physician


def addComplaint(request):
    if request.method == "POST":
        form = complaintForm(request.POST)
        if form.is_valid():
            complaint = Complaints(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            complaint.patient_id = Patient.objects.get(id=request.session['user'])
            complaint.save()
            message = 'Complaint registered successfully'
            para = {'form': form, "message": message}
            return render(request, 'USERS/addComplaint.html', para)
        message = 'Invalid Input Try Again'
        para = {'message': message, 'form': form}
        return render(request, 'USERS/addComplaint.html', para)
    form = complaintForm()
    para = {'form': form}
    return render(request, 'USERS/addComplaint.html', para)


def addPhysicianComplaint(request):
    if request.method == "POST":
        form = physicianComplaintForm(request.POST)
        if form.is_valid():
            complaint = physicianComplaints(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            complaint.physician_id = Physician.objects.get(id=request.session['user'])
            complaint.save()
            message = 'Complaint registered successfully'
            para = {'form': form, "message": message}
            return render(request, 'USERS/physicianComplaint.html', para)
        message = 'Invalid Input Try Again'
        para = {'message': message, 'form': form}
        return render(request, 'USERS/physicianComplaint.html', para)
    form = complaintForm()
    para = {'form': form}
    return render(request, 'USERS/physicianComplaint.html', para)