from .models import *
from django.forms import ModelForm
from django import forms


class PlasmaRequestForm(ModelForm):
    """
    This form is used to create a plasma request

    This form displays a input field for the patient's name,
                        a drop down menu for the patient's gender,
                        a drop down menu for the plasma group,
                        a input field for plasma quantity,
                        a check box to mark the request as emergency,
                        a date field for the date when the plasma is needed,
                        a textfiled for the address,
                        a input field for the phone number,
                        a textfield for the notes,
                        a button to save the request.

    """
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES))
    needed_within = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PlasmaRequestModel
        fields = '__all__'
        exclude = ['user', 'is_active']
