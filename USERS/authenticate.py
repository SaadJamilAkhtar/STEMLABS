from .models import Patient, Physician, Admin, user
from django import forms
from django.core import serializers


def AuthPassword(password1, password2):
    if password1 == password2:
        return False
    return True


def CheckPassword(password):
    if not password.isalpha() and not password.isnumeric():
        return True
    return False


class CreateAuth():
    def AuthPatient(self, form):
        try:
            patient = user.objects.get(username=form.cleaned_data['user_name'])
        except:
            patient = None
        if not patient:
            return True
        return False

    def AuthPhysician(self, form):
        try:
            physician = user.objects.get(username=form.cleaned_data['user_name'])
        except:
            physician = None
        if not physician:
            return True
        return False


class LogInAuth():
    def userAuth(self, form, request):
        try:
            user_ = user.objects.get(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        except:
            user_ = None
        if user_:
            request.session["type"] = user_.user_type
            request.session["primary_key"] = user_.primary_key
            return True
        return None

    def AuthPatientLogIn(self, pk, request):
        try:
            User = Patient.objects.get(id=int(pk))
            request.session['user'] = User.id
            return True
        except:
            return False


    def AuthPhysicianLogIn(self, pk, request):
        try:
            User = Physician.objects.get(id=int(pk))
            request.session['user'] = User.id
            return True
        except:
            return False

    def AuthAdminLogIn(self, form, request):
        try:
            User = Admin.objects.get(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            request.session['user'] = User.id
            return True
        except:
            return False
