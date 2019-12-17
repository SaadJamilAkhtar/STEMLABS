from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import *
from PATIENT.views import checkTests, checkProgress
from LAB.views import makeAppointment
from NEWS_FEED.views import showNews
from COMPLAIN.views import addComplaint, addPhysicianComplaint
from PHYSICIAN.views import checkAppointments, updateProgress, physicianNews, editEquipment, checkEquipments
from ADMIN.views import checkPhysicians
urlpatterns = [
    path('signIn', LogIn, name='LogIn'),
    path('signUp', createPatient, name='signUp'),
    path('logout', logOut, name='logout'),
    path('edituser', editPatient, name='edit_patient'),
    path('editphysician', editphysician, name='edit_phy'),
    path('About', About, name='About'),
    path('Home', patientHome, name='patient_home'),
    path('services', checkTests, name='services'),
    url(r'^makingAppointment/(?P<testId>\d+)$', makeAppointment),
    path('history', checkProgress, name='history'),
    path('news', showNews, name='news'),
    path('complaint', addComplaint, name='complaint'),
    path('physicianHome', physicianHome, name='phy_home'),
    path('showAppointments', checkAppointments, name='ch_appointments'),
    url(r'^patientProfile/(?P<patientId>\d+)$', profilePatient),
    url(r'^editAppointment/(?P<appointmentId>\d+)$', updateProgress),
    path('physicianNews', physicianNews, name='ch_appointments'),
    path('physicianComplaint', addPhysicianComplaint, name='phy_com'),
    path('checkEquipment', checkEquipments, name='ch_equip'),
    url(r'^editEquipment/(?P<equipmentId>\d+)$', editEquipment, name='edit_equip'),
    path('adminHome', adminHome, name='adminHome'),
    path('addPhysicians', createPhysician, name='add_physician'),
    path('', testing, name='test')

]
