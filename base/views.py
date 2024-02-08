from imaplib import _Authenticator
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from base.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    context = {}
    event_dates = EventDates.objects.filter(type="home").order_by('-event_start').first()
    # print(event_dates)
    msg = "Esummit has ended"
    time_diff = -1
    end = True
    if event_dates is not None:
        current_time = timezone.now()
        time_diff = 0
        end = False
        if event_dates.event_start > current_time:
            # hunt is yet to begin
            time_diff = (event_dates.event_start - current_time).total_seconds()
            msg = "E-summit Starts in"
        elif event_dates.event_end > current_time:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "E-summit Ends in"
        else:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "E-summit has ended"
            end = True
    context['msg'] = msg
    context['time_diff'] = int(time_diff)
    context['has_ended'] = end
    return render(request,'home.html',context)

def handleLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve user object by email
        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request, 'No user found with this email address.')
            return redirect('/login')

        # Authenticate user with email and password
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('/details')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('/register')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')


    


def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration.html', {'error_message': 'Passwords do not match'})

        # Check if username is already taken
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'Username is already taken'})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('/login')  # Redirect to the home page after successful registration
    else:
        return render(request, 'register.html')
