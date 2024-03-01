from . views import *
from django.urls import path
from django.urls import path,include


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('login', handleLogin, name='handleLogin'),
    path('register', handleSignUp, name='handleSignUp'),
    path('verify', verify, name='verify'),
    path('merch',merch, name='merch'),
    path('passes',passes, name='passes')

]