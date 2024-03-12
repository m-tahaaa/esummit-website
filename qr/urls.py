from django.urls import path
from qr.views import *

app_name = 'qr'
urlpatterns = [
    path('home', home, name='home'),
    path('profile', profile, name="profile"),
    path('scanner', scanner, name="scanner"),
    # path('scan/', scan, name='scan'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]