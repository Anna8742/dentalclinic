from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_email', 'appointment_date', 'created_at')
    list_filter = ('appointment_date',)
    search_fields = ('patient_name', 'patient_email')
