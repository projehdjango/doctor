from django.shortcuts import render,redirect
from django.views import View
from .models import Doctor, Appointment
from datetime import datetime, timedelta

class CreateAppointmentsView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'create_appointment.html', {'doctors': doctors})

    def post(self, request):
        doctor_id = request.POST.get('doctor')
        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        start_time = datetime.strptime(request.POST.get('start_time'), '%H:%M').time()
        end_time = datetime.strptime(request.POST.get('end_time'), '%H:%M').time()

        doctor = Doctor.objects.get(id=doctor_id)
        doctor.create_appointments(start_date, end_date, start_time, end_time)

        return render(request, 'appointment_success.html')


class ReserveAppointmentView(View):
    def get(self, request):
        appointments = Appointment.objects.filter(is_reserved=False)
        return render(request, 'reserved_appointments.html', {'appointments': appointments})

    def post(self, request):
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.patient = request.user
        appointment.is_reserved = True
        appointment.save()
        return redirect('reserved_appointments')
