from django.contrib import admin
from django.urls import path, include
from . import views
# from django.contrib import messages
# from django.shortcuts import redirect
# messages.info(request,'message')
# return redirect(view)
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    ]