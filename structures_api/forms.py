from django import forms
from django.contrib.admin import widgets

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['airspace_structure',
                  'lower_limit',
                  'upper_limit',
                  'activation_date',
                  'deactivation_date',
                  'activation_time',
                  'deactivation_time',
                  ]
        widgets = {
            'activation_date': forms.SelectDateWidget(),
            'deactivation_date': forms.SelectDateWidget(),
            'activation_time': forms.TimeInput(),
            'deactivation_time': forms.TimeInput(),
        }


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
