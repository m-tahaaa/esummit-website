from django.shortcuts import render,redirect
from hunt.models import *
from gamers.views import prepare_context
from base.models import EventDates
from django.utils import timezone
from django.contrib import messages
from gamers.models import *
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

def get_successfull_scans(request):
    gamer = Gamer.objects.get(user=request.user)
    scans_list = SuccessfullScan.objects.all().filter(gamer=gamer)
    return scans_list

# Create your views here.
def home(request):
    context = prepare_context(request)
    event_dates = EventDates.objects.filter(type="hunt").order_by('-event_start').first()
    # print(event_dates)
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
    return render(request,'hunt/home.html',context)

@login_required
def scanner(request):
    context = {}
    context = prepare_context(request)
    if request.method == 'POST':
        qr_code = request.POST.get('qr-code')
        # print(qr_code)
        if qr_code:
            try:
                qr_scan = QRScan.objects.get(code = qr_code)
            except QRScan.DoesNotExist:
                qr_scan = None
            if qr_scan is not None:
                # check if user is club member if yes text if scan exists and reply saying so
                if context['is_club_member']:
                    messages.success(request,"QR works, you can learn more about the qr in manage QR panel.")
                    return redirect('/gamers/profile')
                # check if user has scanned it once already if yes show message and dont allow more scans
                successfull_scans = get_successfull_scans(request)
                for s_scan in successfull_scans:
                    if s_scan.qr_code_id == qr_scan.id:
                        # trying to scan again
                        messages.info(request,'You have already scanned this QR.')
                        return redirect('/gamers/profile')
                if qr_scan.count == 0:
                    # scanned for the first time give max points and save
                    successfull_scan = SuccessfullScan()
                    successfull_scan.gamer = Gamer.objects.get(user=request.user)
                    successfull_scan.qr_code_id = qr_scan.id
                    successfull_scan.points_given = qr_scan.points_max
                    successfull_scan.save()
                    qr_scan.count = qr_scan.count + 1
                    qr_scan.save()
                    messages.success(request,"Congrats you succesfully scanned the QR. The QR was scanned for the first time, so you get "+str(successfull_scan.points_given) +" points!")
                    return redirect('/gamers/profile')
                elif qr_scan.count < 5:
                    # scanned for the first  5time give mid points and save
                    successfull_scan = SuccessfullScan()
                    successfull_scan.gamer = Gamer.objects.get(user=request.user)
                    successfull_scan.qr_code_id = qr_scan.id
                    successfull_scan.points_given = qr_scan.points_mid
                    successfull_scan.save()
                    qr_scan.count = qr_scan.count + 1
                    qr_scan.save()
                    messages.success(request,"Congrats you succesfully scanned the QR. The QR was scanned for the "+str(qr_scan.count)+" time(s), so you get "+str(successfull_scan.points_given) +" points!")
                    return redirect('/gamers/profile')
                else:
                    # scan is now common give min points and save
                    successfull_scan = SuccessfullScan()
                    successfull_scan.gamer = Gamer.objects.get(user=request.user)
                    successfull_scan.qr_code_id = qr_scan.id
                    successfull_scan.points_given = qr_scan.points_min
                    successfull_scan.save()
                    qr_scan.count = qr_scan.count + 1
                    qr_scan.save()
                    messages.success(request,"Congrats you succesfully scanned the QR. The QR was scanned for the "+str(qr_scan.count)+" time(s), so you get "+str(successfull_scan.points_given) +" points!")
                    return redirect('/gamers/profile')
            else:
                messages.error(request,"The qr you scanned isn't working or is incorrect please scan correctly.")
                return redirect('/gamers/profile')
    return render(request,'hunt/scanner.html',context)


@login_required
def manage_qr(request):
    context = {}
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        context['gamer'] = Gamer.objects.get(user=request.user)
        social_account = SocialAccount.objects.get(user=request.user)
        context['profile_img'] = social_account.extra_data.get('picture')
        context['qr_scans'] = QRScan.objects.all()
        # print(context)
        # print(Gamer.objects.get(user=request.user).user)
    return render(request,'hunt/manage_qr.html',context)

@login_required
def add_qr(request):
    context = {}
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        if request.method == 'POST':
            if 'save-btn' in request.POST:
                if request.POST.get('quantity'):
                    quantity = int(request.POST.get('quantity'))
                else:
                    quantity = 1
                location = request.POST.get('location')
                sponsor = request.POST.get('sponsor')
                while quantity > 0:
                    qr_scan = QRScan()
                    qr_scan.location = location
                    qr_scan.sponsor = sponsor
                    qr_scan.code = 'QR_'+uuid.uuid4().hex[:12].upper()
                    qr_scan.save()
                    quantity = quantity - 1
                messages.success(request,"Succesfully added "+ str(quantity)+" QR(s),Sponsored by "+sponsor)
                return redirect('/hunt/manage_qr')
        # print(Gamer.objects.get(user=request.user).user)
    return render(request,'hunt/add_qr.html',context)

def detail_qr(request, qr_id):
    context = {}
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        qr_scan = QRScan.objects.get(id=qr_id)
        context['scan'] = qr_scan
    return render(request,'hunt/qr_detail.html',context)

@login_required
def delete_qr(request, qr_id):
    context = {}
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        qr_scan = QRScan.objects.get(id=qr_id)
        code = qr_scan.code
        qr_scan.delete()
        messages.success(request,"Succesfully deleted QR, QR_VAL="+str(code))
        return redirect('/hunt/manage_qr')

def edit_qr(request, qr_id):
    context = {}
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        qr_scan = QRScan.objects.get(id=qr_id)
        context['scan'] = qr_scan
        if request.method == 'POST':
            if 'save-btn' in request.POST:
                qr_scan.location = request.POST.get('location')
                qr_scan.sponsor = request.POST.get('sponsor')
                qr_scan.save()
                messages.success(request,"Succesfully edited QR, QR_VAL="+str(qr_scan.code))
                return redirect('/hunt/manage_qr')
        return render(request,'hunt/edit_qr.html',context)