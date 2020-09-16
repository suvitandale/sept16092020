from django.contrib import admin
from django.urls import path
from .views import login,signup,home

print('This is my 1st+1 by git change')
print('This is my 2nd+2 by git change')
print('This is my 3rd+3 by git change')

urlpatterns = [
    path('',home.index,name='homepage'),
    path('signup',signup.SignupView.as_view(),name='signup'),
    path('login',login.LoginView.as_view(),name='login'),
]
