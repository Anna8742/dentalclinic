from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"

    class Meta:
        ordering = ['appointment_date']
        unique_together = ('appointment_date',)
