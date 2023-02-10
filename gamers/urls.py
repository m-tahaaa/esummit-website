from django.urls import path
from gamers.views import *

app_name = 'gamers'
urlpatterns = [
    path('profile/', profile,name='profile'),
    path('register/', register,name='register'),
    path('leaderboard/', leaderboard,name='leaderboard'),
]