from django.urls import path
from qr.views import *

app_name = 'qr'
urlpatterns = [
    path('', home, name='home'),
    path('scan/', scan, name='scan'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]