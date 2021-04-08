from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('',views.signup,name='signup'),
    path('signupr', views.signupr, name='signupr'),


]
