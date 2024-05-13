from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .forms import AppointmentForm
from .models import Appointment

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['date']
            appointment_time = form.cleaned_data['time']
            
            # Check if appointment already exists for the selected date and time
            if Appointment.objects.filter(date=appointment_date, time=appointment_time).exists():
                # Handle double booking scenario
                return render(request, 'scheduler/double_booking_error.html')
            
            # If no double booking, proceed to save the appointment
            appointment = form.save()  # Save the form data to the database

            # Get the confirmation date and time
            confirmation_date_time = timezone.now()

            # Send email confirmation
            send_mail(
                'Appointment Confirmation',
                f'Your appointment has been scheduled successfully on {appointment.date} at {appointment.time}. Confirmation received at {confirmation_date_time}.',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            # Send email to admin
            send_mail(
                'New Appointment Booked',
                f'A new appointment has been booked on {appointment.date} at {appointment.time} by {appointment.first_name}.',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Redirect to the success page
            return redirect('appointment_success')
    else:
        form = AppointmentForm()

    return render(request, 'scheduler/schedule_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'scheduler/appointment_success.html')

def double_booking_error(request):
    return render(request, 'scheduler/double_booking_error.html')




# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from .forms import AppointmentForm  # Assuming you have created a form for the appointment details

# from django.conf import settings
# from django.contrib import messages
#from django.shortcuts import render, redirect
# from .forms import AppointmentForm,Appointment
# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
# from django.urls import reverse



# email_host_user = settings.EMAIL_HOST_USER


# def schedule_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             # Check if the selected date and time are available
#             if not AppointmentForm.objects.filter(date_time=appointment.date_time).exists():
#                 appointment.save()
#                 # Send email confirmation
#                 subject = request.POST('Appointment Confirmation')
#                 message = request.POST('Your appointment has been booked successfully.')
#                 email = request.POST(settings.EMAIL_HOST_USER)
#                 recipient_list = [appointment_success.email,]
#                 # recipient_list = [appointment.email,settings.EMAIL_HOST_USER]
#                 send_mail(
#                     subject,
#                     message,
#                     email,
#                     recipient_list,
#                     fail_silently=True,
#                 )
#                 return redirect('appointment_success')
#             else:
#                 return render(request, 'scheduler/schedule_appointment.html', {'form': form, 'error_message': 'This time slot is already booked. Please choose another.'})
#     else:
#         form = AppointmentForm()
#     return render(request, 'scheduler/schedule_appointment.html', {'form': form})

# def appointment_success(request):
#     return render(request, 'scheduler/appointment_success.html')


