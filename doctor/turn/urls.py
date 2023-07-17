from django.urls import path
from .views import CreateAppointmentsView,ReserveAppointmentView
app_name='turn'
urlpatterns = [
    # ...
    path('create/', CreateAppointmentsView.as_view(), name='create_appointment'),
    path('reserv/', ReserveAppointmentView.as_view(), name='reserved_appointments'),
    # ...
]