from . import views
from django.urls import path
from django.urls import path,include


app_name = 'base'
urlpatterns = [
    path('', views.home,name='home'),
    path('login',views.handleLogin,name='handleLogin'),
    path('register',views.handleSignUp,name='handleSignUp')

]