#list().create,retrive, update ,delete
from rest_framework import viewsets
from . import models
from . import serializer
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.employee.objects.all()
    serializer_class = serializer.employeeserializer