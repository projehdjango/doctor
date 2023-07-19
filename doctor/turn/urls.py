from django.urls import path
from .views import CreateAppointmentsView,ReserveAppointmentView,doctor_delay_view,ReservedAppointments_listView
app_name='turn'
urlpatterns = [
    # ...
    path('create/', CreateAppointmentsView.as_view(), name='create_appointment'),
    path('reserved_appointments/', ReserveAppointmentView.as_view(), name='reserved_appointments'),
    path('delay/', doctor_delay_view.as_view(), name='doctor_delay'),
    path('reserved_list/',ReservedAppointments_listView.as_view(), name='reserved_list'),
    # ...
    # ...
]