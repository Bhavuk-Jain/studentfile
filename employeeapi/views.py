from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employee

def employee_list(request):
    if request.method == 'POST':
        us = request.POST['username']
        ps = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(username=us, password=ps)
        if x is None:

            return HttpResponse('Password is Wrong')

        else:
            context = employee.objects.all()
            print(context)

            return render(request, 'employee_list.html', {'Employee':context})

def employee_delete(request):
    return redirect('admin/')
