from .models import User,Appointment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'