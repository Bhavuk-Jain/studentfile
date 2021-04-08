#two way communication respose and request ,external app from any device is able to communnicate with api present here
from rest_framework import serializers
from .models import employee

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields ='__all__'