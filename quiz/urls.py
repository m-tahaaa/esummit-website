from django.urls import path
from quiz.views import *

app_name = 'quiz'
urlpatterns = [
    path('', home,name='home'),
    path('play/', play_quiz,name='play'),
    path('manage/', manage,name='manage'),
    # path('add_qr/', add_qr,name='add_qr'),
    # path('detail_qr/<int:qr_id>', detail_qr,name='qr_detail'),
    # path('delete_qr/<int:qr_id>', delete_qr,name='delete_qr'),
    # path('edit_qr/<int:qr_id>', edit_qr,name='edit_qr'),
]