from django.shortcuts import render,redirect
from gamers.models import *
from django.contrib import messages
from allauth.socialaccount.models import SocialAccount
import uuid
from django.contrib.auth.decorators import login_required

def get_code():
    return 'H_'+uuid.uuid4().hex[:8].upper()

def get_successfull_scans(request):
    gamer = Gamer.objects.get(user=request.user)
    scans_list = SuccessfullScan.objects.all().filter(gamer=gamer)
    return scans_list

def get_gamers_list()->list:
    gamers_list = []
    for gamer in Gamer.objects.all():
        gamers_list.append(gamer.user)
    return gamers_list

def get_clubmember_list()->list:
    member_list = []
    for member in ClubMember.objects.all():
        member_list.append(member.user)
    return member_list

# def get_successfull_scans(request):
#     gamer = Gamer.objects.get(user=request.user)
#     scans_list = SuccessfullScan.objects.all().filter(gamer=gamer)
#     return scans_list

def prepare_context(request):
    context = {}
    is_game_user = request.user in get_gamers_list()
    is_club_member = request.user in get_clubmember_list()
    context['is_game_user'] = is_game_user
    context['is_club_member'] = is_club_member
    return context

def get_key(gamer):
    # print(gamer['get_total_points'])
    return int(gamer['get_total_points'])

def order_by_points():
    gamers = Gamer.objects.all().order_by('-points','user__first_name')
    # print(gamers)
    gamers_list = []
    for gamer in gamers:
        if gamer.user in get_clubmember_list():
            # user is a club member
            continue
        new_gamer = {}
        social_account = SocialAccount.objects.get(user=gamer.user)
        new_gamer['profile_img'] = social_account.extra_data.get('picture')
        new_gamer['user'] = gamer.user
        new_gamer['phone'] = gamer.phone
        new_gamer['college'] = gamer.college
        new_gamer['referral_code'] = gamer.referral_code
        new_gamer['points'] = gamer.points
        new_gamer['get_total_points'] = gamer.get_total_points
        new_gamer['share_code'] = gamer.share_code
        gamers_list.append(new_gamer)
    # print(gamers_list)
    gamers_list.sort(key=get_key,reverse=True)
    # print(gamers_list)
    return gamers_list

def get_rank(request):
    gamers = order_by_points()
    rank = 1
    for gamer in gamers:
        if gamer['user'] == request.user:
            break;
        rank = rank + 1
    return rank

# Create your views here.
@login_required
def profile(request):
    context = {}
    context = prepare_context(request)
    if not context['is_game_user']:
        # tell to register as a game user and then start playing
        messages.info(request,"Please register as a gamer before starting to play")
        return redirect('/gamers/register')
    else:
        context['gamer'] = Gamer.objects.get(user=request.user)
        social_account = SocialAccount.objects.get(user=request.user)
        gamers = Gamer.objects.all().order_by('points','user__first_name')
        context['profile_img'] = social_account.extra_data.get('picture')
        context['gamers_count'] = len(order_by_points())
        context['rank'] = get_rank(request)
        context['scans'] = get_successfull_scans(request)
        context['responses'] = QuizResponse.objects.filter(gamer=context['gamer'])
    return render(request,'gamers/profile.html',context)

@login_required
def register(request):
    context = {}
    context = prepare_context(request)
    if context['is_game_user']:
        return redirect('/game/profile')
    if context['is_club_member']:
        return redirect('/game/profile')
    if request.method == 'POST':
        if 'save-btn' in request.POST:
            # got some data in POST, create the gamer, save and redirect to profile page with a message
            new_gamer = Gamer()
            new_gamer.user = request.user
            new_gamer.college = request.POST.get('college')
            new_gamer.phone = request.POST.get('phone')
            new_gamer.share_code = 'H_'+uuid.uuid4().hex[:8].upper()
            # print("college: "+ new_gamer.college)
            # if ref code in valid ref code points+ 10 for both parties
            # check if ref-code is not empty
            if request.POST.get('ref-code')!='':
                # we got a referral code, lets check if its valid
                share_code = request.POST.get('ref-code')
                share_code = str(share_code).upper()
                gamers = Gamer.objects.all().filter(share_code =share_code)
                if gamers.count() == 0:
                    messages.info(request,"The share code you enterred is not correct, please enter correctly or try register without the share code.")
                    return redirect('/game/register')
                else:
                    share_gamer = gamers.first()
                    share_gamer.points += 10
                    share_gamer.save()
                    new_gamer.points = 10
                    messages.info(request,"The share code you enterred is correct")
            # print('ref-code:',request.POST.get('ref-code')=='')
            new_gamer.save()
            messages.success(request,'You have completed registration now you can start playing and get prizes!')
            return redirect('/gamers/profile')
    return render(request,'gamers/register.html')

def leaderboard(request):
    context = {}
    context = prepare_context(request)
    ordered = order_by_points()
    # for gamer in ordered:
    #     print(gamer.get('user__first_name'),gamer.get('points'))
    context['gamers'] = ordered
    return render(request,'gamers/leaderboard.html',context)