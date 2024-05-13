from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'email', 'date', 'time']



# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['date_time']
