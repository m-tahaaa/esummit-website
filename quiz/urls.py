from django.urls import path
from quiz.views import *

app_name = 'quiz'
urlpatterns = [
    path('', home,name='home'),
    path('play/', play_quiz,name='play'),
    path('manage/', manage,name='manage'),
    path('mark_answer_correct/<int:response_id>', mark_answer_correct,name='mark_answer_correct'),
    path('mark_answer_wrong/<int:response_id>', mark_answer_wrong,name='mark_answer_wrong'),
    path('detail/<int:q_id>', detail_q,name='detail'),
]