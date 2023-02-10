from django.urls import path
from hunt.views import *

app_name = 'hunt'
urlpatterns = [
    path('', home,name='home'),
    path('scanner/', scanner,name='scanner'),
    path('manage_qr/', manage_qr,name='manage_qr'),
    path('add_qr/', add_qr,name='add_qr'),
    path('detail_qr/<int:qr_id>', detail_qr,name='qr_detail'),
    path('delete_qr/<int:qr_id>', delete_qr,name='delete_qr'),
    path('edit_qr/<int:qr_id>', edit_qr,name='edit_qr'),
]