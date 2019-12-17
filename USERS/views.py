from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm, PhysicianForm, LogInForm, PatientEditForm, PhysicianEditForm
from .authenticate import AuthPassword, LogInAuth, CreateAuth
from .models import Patient, Physician, Admin, user


def Home(request):
    return render(request, 'index.html')


def logOut(request):
    request.session.flush()
    return redirect('../')


def patientHome(request):
    User = Patient.objects.get(id=request.session['user'])
    full_name = User.first_name + ' ' + User.last_name
    message = 'Welcome %s' % (
        (User.first_name + ' ' + User.last_name))
    para = {'message': message, 'user': User, 'name': full_name}
    return render(request, 'USERS/patientHome.html', para)


def adminHome(request):
    User = Admin.objects.get(id=request.session['user'])
    full_name = User.first_name + ' ' + User.last_name
    message = 'Welcome %s' % (
        (User.first_name + ' ' + User.last_name))
    para = {'message': message, 'user': User, 'name': full_name}
    return render(request, 'USERS/adminHome.html', para)


def physicianHome(request):
    User = Physician.objects.get(id=request.session['user'])
    full_name = User.first_name + ' ' + User.last_name
    message = 'Welcome %s' % (
        (User.first_name + ' ' + User.last_name))
    para = {'message': message, 'user': User, 'name': full_name}
    return render(request, 'USERS/physicianHome.html', para)


def About(request):
    return render(request, 'USERS/About.html')


def testing(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            if form.save():
                return HttpResponse('HO GYA')
            else:
                return HttpResponse('NAI HOA')
        return HttpResponse('Valid nai')
    else:
        form = PatientForm()
        return render(request, 'USERS/test.html', {'form': form})  # YE CHAWAL BAD MAI DELETE KAR DAIN


def createPatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            auth = CreateAuth()
            if auth.AuthPatient(form):
                if AuthPassword(form.cleaned_data['password'], form.cleaned_data['re_password']):
                    message = 'Passwords Do not Match'
                    para = {'message': message, 'form': form}
                    return render(request, 'USERS/signUp.html', para)  # ADD LOGIN REDIRECT HERE
                user_ = form.save()
                userTable = user(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'],
                                 primary_key=user_.id, user_type='patient')
                userTable.save()
                if user_:
                    message = "User Created Successfully"
                    para = {'message': message}
                    return render(request, 'USERS/signUp.html', para)  # ADD LOGIN REDIRECT HERE
                else:
                    message = "An unexpected error occurred please try again"
                    para = {'message': message, 'form': form}
                    return render(request, 'USERS/signUp.html', para)  # ADD A SIGNUP REDIRECT HERE
            else:
                message = "Username is Already Taken Please Enter Another Username"
                para = {'message': message, 'form': form}
                return render(request, 'USERS/signUp.html', para)  # ADD A SIGNUP REDIRECT HERE
        else:
            message = 'Invalid Input Please Try Again'
            para = {'message': message, 'form': form}
            return render(request, 'USERS/signUp.html', para)  # ADD A SIGNUP REDIRECT HERE
    else:
        form = PatientForm()
        para = {'form': form}
        return render(request, 'USERS/signUp.html', para)  # ADD A SIGNUP REDIRECT HERE


def editPatient(request):
    User = Patient.objects.get(id=int(request.session['user']))
    form = PatientEditForm(instance=User)
    if request.method == 'POST':
        filled_form = PatientEditForm(request.POST, request.FILES, instance=User)
        if filled_form.is_valid():
            filled_form.save()
            User = Patient.objects.get(id=request.session['user'])
            full_name = User.first_name + ' ' + User.last_name
            message = 'Welcome %s' % (
                (User.first_name + ' ' + User.last_name))
            para = {'message': message, 'user': User, 'name': full_name}
            return render(request, 'USERS/patientHome.html', para)
    return render(request, 'USERS/editUser.html', {'form': form})


def editphysician(request):
    User = Physician.objects.get(id=int(request.session['user']))
    form = PhysicianEditForm(instance=User)
    if request.method == 'POST':
        filled_form = PhysicianEditForm(request.POST, request.FILES, instance=User)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('./physicianHome')
    return render(request, 'USERS/editUser.html', {'form': form})


def createPhysician(request):
    if request.method == 'POST':
        form = PhysicianForm(request.POST, request.FILES)
        if form.is_valid():
            auth = CreateAuth()
            if auth.AuthPhysician(form):
                if AuthPassword(form.cleaned_data['password'], form.cleaned_data['re_password']):
                    message = 'Passwords Do not Match'
                    para = {'message': message, 'form': form}
                    return render(request, 'USERS/addPhysician.html', para)  # ADD A SIGNUP REDIRECT HERE
                user_ = form.save()
                userTable = user(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'],
                                 primary_key=user_.id, user_type='physician')
                userTable.save()
                if user_:
                    form = PhysicianForm()
                    message = "User Created Successfully"
                    para = {'message': message, 'form': form}
                    return render(request, "USERS/addPhysician.html", para)  # ADD LOGIN REDIRECT HERE
                else:
                    message = "An unexpected error occurred please try again"
                    para = {'message': message, 'form': form}
                    return render(request, 'USERS/addPhysician.html', para)  # ADD A SIGNUP REDIRECT HERE
            else:
                message = "Username is Already Taken Please Enter Another Username"
                para = {'message': message, 'form': form}
                return render(request, 'USERS/addPhysician.html', para)  # ADD A SIGNUP REDIRECT HERE

        else:
            message = 'Invalid Input Please Try Again'
            para = {'message': message, 'form': form}
            return render(request, 'USERS/addPhysician.html', para)  # ADD A SIGNUP REDIRECT HERE
    else:
        form = PhysicianForm()
        para = {'form': form}
        return render(request, 'USERS/addPhysician.html', para)  # ADD A SIGNUP REDIRECT HERE


def LogIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            auth = LogInAuth()
            users = auth.userAuth(form, request)
            if users:
                if request.session['type'] == 'patient':
                    if auth.AuthPatientLogIn(request.session['primary_key'], request):
                        User = Patient.objects.get(id=request.session['user'])
                        full_name = User.first_name + ' ' + User.last_name
                        message = 'Welcome %s' % (
                            (User.first_name + ' ' + User.last_name))
                        para = {'message': message, 'user': User, 'name': full_name}
                        return render(request, 'USERS/patientHome.html', para)  # ADD LOGEDIN PATIENT REDIRECT
                if request.session['type'] == 'physician':
                    if auth.AuthPhysicianLogIn(request.session['primary_key'], request):
                        User = Physician.objects.get(id=request.session['user'])
                        full_name = User.first_name + ' ' + User.last_name
                        message = 'Welcome %s' % (
                            (User.first_name + ' ' + User.last_name))
                        para = {'message': message, 'user': User, 'name': full_name}
                        return render(request, 'USERS/physicianHome.html', para)  # ADD LOGEDIN PATIENT REDIRECT
            if auth.AuthAdminLogIn(form, request):
                User = Admin.objects.get(id=request.session['user'])
                message = 'Welcome %s' % (
                    (User.first_name + ' ' + User.last_name))
                para = {'message': message, 'user': User, 'name': (User.first_name + ' ' + User.last_name)}
                return render(request, 'USERS/adminHome.html', para)  # ADD ADMIN LOGED_IN PATIENT REDIRECT

            else:
                form = LogInForm()
                message = 'No such user exists'
                para = {'message': message, 'form': form}
                return render(request, 'USERS/signIn.html', para)  # ADD LOGIN_FORM PATIENT REDIRECT
        else:
            form = LogInForm()
            message = 'Invalid input please try again'
            para = {'message': message, 'form': form}
            return render(request, 'USERS/signIn.html', para)  # ADD LOGIN_FORM PATIENT REDIRECT
    else:
        form = LogInForm()
        para = {'form': form}
        return render(request, 'USERS/signIn.html', para)  # ADD LOGIN_FROM HERE


def profilePatient(request, patientId):
    patient = Patient.objects.get(id=int(patientId))
    name = patient.first_name + ' ' + patient.last_name
    para = {'patient': patient, 'name': name}
    return render(request, 'USERS/profile.html', para)
