from django.shortcuts import render
from base.models import *
from django.utils import timezone
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
    return render(request,'base/home.html',context)