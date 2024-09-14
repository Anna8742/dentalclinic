from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Appointment
from .forms import AppointmentForm

def index(request):
    return render(request, 'index.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            # Check if the slot is available
            if not Appointment.objects.filter(appointment_date=appointment.appointment_date).exists():
                appointment.save()
                return redirect('index')
            else:
                form.add_error(None, "This slot is already booked.")
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})
