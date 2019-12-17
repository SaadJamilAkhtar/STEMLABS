from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, null=False)
    cnic = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=6, null=False)
    age = models.CharField(max_length=3, null=False)
    image = models.ImageField(upload_to='images/profile', default='images/profile/default_profile_image.jpg')


class Patient(Users):
    blood_group = models.CharField(max_length=3)
    height = models.IntegerField()
    weight = models.IntegerField()
    is_patient = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Physician(Users):
    date_joined = models.DateField()
    is_physician = models.BooleanField(default=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Admin(Users):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False, default='Admin')
    password = models.CharField(max_length=50, null=False, blank=False, default='STEMLABS')
    is_admin = models.BooleanField(default=True)


class user(models.Model):
    user_choices = [('patient', 'patient'), ('physician', 'physician')]
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    primary_key = models.IntegerField()
    user_type = models.CharField(max_length=10, choices=user_choices)
