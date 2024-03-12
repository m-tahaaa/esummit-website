from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render,redirect
from base.models import EventDates
from django.utils import timezone
from . models import *
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

BONUS_POINTS = 25

def checkBonus(collection, card):
    bonus = False

    tier_score_initial = 1;
    for i in collection[card.tier] :
        tier_score_initial *= i

    collection[card.tier][card.identity]+=1

    tier_score_final = 1;
    for i in collection[card.tier] :
        tier_score_final *= i
    
    if tier_score_initial == 0 and tier_score_final != 0 :
        bonus = True
    
    return bonus

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

def leaderboard(request):
    profiles = Profile.objects.all().order_by('points')
    return render(request, 'qr/leaderboard.html', {'profiles': profiles})

@login_required
def scan(request, code):
    context = {}
    profile = Profile.objects.get(user=request.user)
    qr = Qr.objects.get(uniqueId=code)
    if profile is None :
        return redirect('/qr/profile')
    context['profile'] = profile

    card = qr.card
    context['card'] = card

    duplicate = Scan.objects.filter(profile=profile, qr=qr).exists()
    if duplicate :                      # check for duplicate
        context['duplicate'] = duplicate
        messages.error(request, 'You have already scanned this qr')
        return render(request, 'qr/scan.html', context)
    
    Scan.objects.create(profile=profile,qr=qr)     # if not duplicate

    profile.points += card.point  #card point added

    collection_obj = json.loads(profile.collections)

    bonus = checkBonus(collection_obj, card)
    if bonus :
        profile.points += BONUS_POINTS
    context['bonus'] = bonus

    profile.collections = json.dumps(collection_obj)

    profile.save()

    return render(request, 'qr/scan.html', context)
 
@login_required 
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    
    if profile is None :
        messages.info(request, 'Please register first')
        return redirect('/qr/register')
    
    context = {'profile' : profile}

    rank = Profile.objects.filter(points__lt = profile.points).count() + 1
    context['rank'] = rank

    cards = Card.objects.all()
    context['cards'] = cards

    collection = json.loads(profile.collections)
    context['collection'] = collection
    print(context['collection'])
    return render(request, 'qr/profile.html', context)

@login_required
def register(request):
    if request.method == 'POST' :
        profile = Profile.objects.create(
            user=request.user,
            name = request.POST.get('name'),
            picture='https://ui-avatars.com/api/?name=' + user.first_name + '+' + user.last_name + '&background=fdba74&color=282319',
            email = request.POST.get('email'),
            mobile = request.POST.get('phone_number'),
            registration = request.POST.get('reg'),
        )

        return redirect('/qr/profile')

    if Profile.objects.filter(user=request.user).exists():
        messages.info(request, 'You have already registered')
        return redirect(request, 'qr/profile')
    return render(request, 'qr/register.html')

@login_required
def scanner(request):
    profile = Profile.objects.get(user=request.user)
    if profile is None:
        return redirect('/qr/profile')
    return render(request, 'qr/scanner.html')