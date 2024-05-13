
from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    first_name = models.CharField(max_length=100, default='John')
    email = email = models.EmailField(default='example@example.com')
    date =models.DateField(default=timezone.now)
    time = models.TimeField(default='09:00')


# from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.user.name} - {self.date_time}"


