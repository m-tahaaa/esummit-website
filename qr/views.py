from django.shortcuts import render,redirect
from base.models import EventDates
from django.utils import timezone

# Create your views here.

def home(request):
    # context = prepare_context(request)
    event_dates = EventDates.objects.filter(type="hunt").order_by('-event_start').first()
    # print(event_dates)
    context ={}
    msg = "Hunt has ended"
    time_diff = -1
    end = True
    if event_dates is not None:
        current_time = timezone.now()
        time_diff = 0
        end = False
        if event_dates.event_start > current_time:
            # hunt is yet to begin
            time_diff = (event_dates.event_start - current_time).total_seconds()
            msg = "Hunt Starts in"
        elif event_dates.event_end > current_time:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "Hunt Ends in"
        else:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "Hunt has ended"
            end = True
    context['msg'] = msg
    context['time_diff'] = int(time_diff)
    context['has_ended'] = end
    return render(request,'qr/home.html',context)
    # return render(request, 'qr/home.html')

def profile(request):
    return render(request,'qr/profile.html')
