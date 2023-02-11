from django.shortcuts import render,redirect
from gamers.views import prepare_context
from base.models import EventDates
from django.utils import timezone
from django.contrib import messages
from quiz.models import *
from gamers.models import QuizResponse,Gamer
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

# Create your views here.
def home(request):
    context = prepare_context(request)
    event_dates = EventDates.objects.filter(type="quiz").order_by('-event_start').first()
    # print(event_dates)
    msg = "Quiz has ended"
    time_diff = -1
    end = True
    if event_dates is not None:
        current_time = timezone.now()
        time_diff = 0
        end = False
        if event_dates.event_start > current_time:
            # hunt is yet to begin
            time_diff = (event_dates.event_start - current_time).total_seconds()
            msg = "Quiz Starts in"
        elif event_dates.event_end > current_time:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "Quiz Ends in"
        else:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "Quiz has ended"
            end = True
    context['msg'] = msg
    context['time_diff'] = int(time_diff)
    context['has_ended'] = end
    return render(request,'quiz/home.html',context)

@login_required
def play_quiz(request):
    context = prepare_context(request)
    msg = "Quiz has ended"
    time_diff = -1
    end = True
    time_msg = "Time left to answer"
    context['has_answered_already'] = False
    current_question = Question.objects.filter(start_date__lte=timezone.now()).filter(end_date__gte=timezone.now()).first()
    if current_question:
        context['current_question_exists'] = True
        # print(current_question)
        msg = 'Answer the Question'
        end = False
        time_diff = (current_question.end_date - timezone.now()).total_seconds()
        if QuizResponse.objects.filter(gamer = Gamer.objects.get(user = request.user)).count() > 0:
            messages.info(request,"You have already answered the currently active question")
            context['has_answered_already'] = True
            next_question = Question.objects.filter(start_date__gte=timezone.now()).first()
            if next_question:
                time_diff = (next_question.start_date - timezone.now()).total_seconds()
                context['next_question_exists'] = True
                time_msg = "Next question goes Live in"
            else:
                time_diff = -1
                time_msg = "There are no more questions. The Quiz has come to an end."
                context['next_question_exists'] = False
        context['question'] = current_question
        if request.method == 'POST':
            if time_diff >= 0:
                # gamer has submitted question in time
                # save his answer and redirect to gamer/profile
                answer_recieved = request.POST.get('answer')
                new_response = QuizResponse()
                new_response.gamer = Gamer.objects.get(user = request.user)
                new_response.question_id = current_question.id
                new_response.points_recieved = current_question.points
                new_response.answer_recieved = answer_recieved
                new_response.save()
                messages.success(request,"You have submitted the answer for the question successfully. The points will be allocated once the current question expires.")
                return redirect('/gamers/profile')
    else:
        context['current_question_exists'] = False
        next_question = Question.objects.filter(start_date__gte=timezone.now()).first()
        if next_question:
            time_diff = (next_question.start_date - timezone.now()).total_seconds()
            context['next_question_exists'] = True
            time_msg = "Next question goes Live in"
            msg = "Please wait for next question to be live"
        else:
            time_diff = -1
            time_msg = "There are no more questions. The Quiz has come to an end."
            context['next_question_exists'] = False
    context['msg'] = msg
    context['time_diff'] = int(time_diff)
    context['has_ended'] = end
    context['time_msg'] = time_msg
    # print(context)
    return render(request,'quiz/play.html',context)

@login_required
def manage(request):
    context = prepare_context(request)
    if not context['is_club_member']:
        # tell to register as a game user and then start playing
        messages.info(request,"Restricted to club members only.")
        return redirect('/gamers/profile')
    else:
        context['gamer'] = Gamer.objects.get(user=request.user)
        social_account = SocialAccount.objects.get(user=request.user)
        context['profile_img'] = social_account.extra_data.get('picture')
        context['questions'] = Question.objects.all()
    return render(request,'quiz/manage.html',context)