from django import forms
from .models import Users, Physician, Patient


# class UserForm(forms.ModelForm):
#     password = forms.CharField(label='PASSWORD', widget=forms.PasswordInput())
#     email = forms.CharField(label='Email', widget=forms.EmailInput())
#
#     class Meta:
#         model = Users
#         fields = ['user_name', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'cnic', 'address',
#                   'gender',
#                   'age', 'image']
#         labels = {'user_name': 'USERNAME', 'password': 'PASSWORD', 'first_name': "FIRST NAME", 'last_name': "LAST NAME",
#                   'email': 'Email',
#                   'phone_number': "PHONE NUMBER", 'cnic': 'CNIC', 'address': 'ADDRESS', 'gender': 'GENDER',
#                   'age': 'AGE', 'image': 'IMAGE'}


class PhysicianForm(forms.ModelForm):
    user_name = forms.CharField(label='USERNAME', widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    re_password = forms.CharField(label='RE-ENTER PASSWORD',
                                  widget=forms.PasswordInput(attrs={'placeholder': 'RE-ENTER PASSWORD'}), min_length=8)
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}),
                               min_length=8)
    phone_number = forms.CharField(label='PHONE NUMBER',
                                   widget=forms.NumberInput(attrs={'placeholder': 'PHONE NUMBER'}))

    class Meta:
        model = Physician
        fields = ['user_name', 'password', 're_password', 'first_name', 'last_name', 'email', 'phone_number', 'cnic',
                  'address',
                  'gender',
                  'age', 'image', 'date_joined', 'experience']
        labels = {'password': 'PASSWORD', 'first_name': "FIRST NAME", 'last_name': "LAST NAME",
                  'email': 'Email',
                  'cnic': 'CNIC', 'address': 'ADDRESS', 'gender': 'GENDER',
                  'age': 'AGE', 'image': 'IMAGE', 'date_joined': "DATE of JOINING", 'experience': 'EXPERIENCE'}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST NAME'}),
            'email': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            'cnic': forms.TextInput(attrs={'placeholder': 'CNIC'}),
            'address': forms.TextInput(attrs={'placeholder': 'ADDRESS'}),
            'gender': forms.TextInput(attrs={'placeholder': 'GENDER'}),
            'age': forms.NumberInput(attrs={'placeholder': 'AGE'}),
            'blood_group': forms.TextInput(attrs={'placeholder': 'BLOOD TYPE'}),
            'date_joined': forms.TextInput(attrs={'placeholder': 'Date Of JOIN (YYYY-MM-DD)'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Experience(Years)'})
        }


class PhysicianEditForm(forms.ModelForm):
    phone_number = forms.CharField(label='PHONE NUMBER',
                                   widget=forms.NumberInput(attrs={'placeholder': 'PHONE NUMBER'}))

    class Meta:
        model = Physician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'cnic',
                  'address',
                  'gender',
                  'age', 'image', 'date_joined', 'experience']
        labels = {'password': 'PASSWORD', 'first_name': "FIRST NAME", 'last_name': "LAST NAME",
                  'email': 'Email',
                  'cnic': 'CNIC', 'address': 'ADDRESS', 'gender': 'GENDER',
                  'age': 'AGE', 'image': 'IMAGE', 'date_joined': "DATE of JOINING", 'experience': 'EXPERIENCE'}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST NAME'}),
            'email': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            'cnic': forms.TextInput(attrs={'placeholder': 'CNIC'}),
            'address': forms.TextInput(attrs={'placeholder': 'ADDRESS'}),
            'gender': forms.TextInput(attrs={'placeholder': 'GENDER'}),
            'age': forms.NumberInput(attrs={'placeholder': 'AGE'}),
            'blood_group': forms.TextInput(attrs={'placeholder': 'BLOOD TYPE'}),
            'date_joined': forms.TextInput(attrs={'placeholder': 'Date Of JOIN (YYYY-MM-DD)'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Experience(Years)'})
        }


class PatientForm(forms.ModelForm):
    user_name = forms.CharField(label='USERNAME', widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    re_password = forms.CharField(label='RE-ENTER PASSWORD',
                                  widget=forms.PasswordInput(attrs={'placeholder': 'RE-ENTER PASSWORD'}), min_length=8)
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}),
                               min_length=8)
    phone_number = forms.CharField(label='PHONE NUMBER',
                                   widget=forms.NumberInput(attrs={'placeholder': 'PHONE NUMBER'}))
    height = forms.IntegerField(label='HEIGHT(in cm)', max_value=250,
                                widget=forms.NumberInput(attrs={'placeholder': 'HEIGHT'}))
    weight = forms.IntegerField(label='WEIGHT(in pound)', max_value=300,
                                widget=forms.NumberInput(attrs={'placeholder': 'WEIGHT'}))

    class Meta:
        model = Patient
        fields = ['user_name', 'password', 're_password', 'first_name', 'last_name', 'email', 'phone_number', 'cnic',
                  'address', 'gender', 'age', 'image', 'blood_group', 'height', 'weight']
        labels = {'password': 'PASSWORD',
                  'first_name': "FIRST NAME", 'last_name': "LAST NAME", 'email': 'Email',
                  'cnic': 'CNIC', 'address': 'ADDRESS', 'gender': 'GENDER',
                  'age': 'AGE', 'image': 'IMAGE', 'blood_group': 'BLOOD GROUP', }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST_NAME'}),
            'email': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            'cnic': forms.TextInput(attrs={'placeholder': 'CNIC'}),
            'address': forms.TextInput(attrs={'placeholder': 'ADDRESS'}),
            'gender': forms.TextInput(attrs={'placeholder': 'GENDER'}),
            'age': forms.NumberInput(attrs={'placeholder': 'AGE'}),
            'blood_group': forms.TextInput(attrs={'placeholder': 'BLOOD TYPE'}),
        }


class PatientEditForm(forms.ModelForm):
    phone_number = forms.CharField(label='PHONE NUMBER',
                                   widget=forms.NumberInput(attrs={'placeholder': 'PHONE NUMBER'}))
    height = forms.IntegerField(label='HEIGHT(in cm)', max_value=250,
                                widget=forms.NumberInput(attrs={'placeholder': 'HEIGHT'}))
    weight = forms.IntegerField(label='WEIGHT(in pound)', max_value=300,
                                widget=forms.NumberInput(attrs={'placeholder': 'WEIGHT'}))

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'cnic',
                  'address', 'gender', 'age', 'image', 'blood_group', 'height', 'weight']
        labels = {'first_name': "FIRST NAME", 'last_name': "LAST NAME", 'email': 'Email',
                  'cnic': 'CNIC', 'address': 'ADDRESS', 'gender': 'GENDER',
                  'age': 'AGE', 'image': 'IMAGE', 'blood_group': 'BLOOD GROUP', }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST_NAME'}),
            'email': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            'cnic': forms.TextInput(attrs={'placeholder': 'CNIC'}),
            'address': forms.TextInput(attrs={'placeholder': 'ADDRESS'}),
            'gender': forms.TextInput(attrs={'placeholder': 'GENDER'}),
            'age': forms.NumberInput(attrs={'placeholder': 'AGE'}),
            'blood_group': forms.TextInput(attrs={'placeholder': 'BLOOD TYPE'}),
        }


class LogInForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
