# scheduler/urls.py
from django.urls import path
#from .views import schedule_appointment, appointment_success
from . import views

urlpatterns = [
    path('schedule/', views.schedule_appointment, name='schedule_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('double-booking-error/', views.double_booking_error, name='double_booking_error'),
]
