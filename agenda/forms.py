from django import forms
from .models import Professional, Service, Appointment, Shift
from django.forms import DateInput, TimeInput

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['name', 'specialty', 'bio', 'photo']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['professional', 'name', 'duration_minutes', 'price']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['professional', 'date', 'start_time', 'end_time', 'max_clients']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['shift', 'service', 'client_name', 'client_phone']
