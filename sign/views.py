from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST' :
        us = request.POST['username']
        em = request.POST['email']
        ps = request.POST['password']
        x=User.objects.create_user(username=us,email=em,password=ps)
        x.save()
        print("user created")
        return redirect('signupr')

    else:
        return render(request,'b.html')
def signupr(request):
    return render(request, 'signupr.html')




