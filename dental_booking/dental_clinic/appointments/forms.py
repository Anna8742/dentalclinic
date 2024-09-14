from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_email', 'appointment_date']

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date.weekday() >= 5:  # Check if the day is Saturday or Sunday
            raise forms.ValidationError("Appointments can only be booked from Monday to Friday.")
        if appointment_date.hour < 9 or appointment_date.hour > 16:  # Ensure slots are between 9 AM to 5 PM
            raise forms.ValidationError("Appointments can only be booked between 9 AM and 5 PM.")
        return appointment_date
