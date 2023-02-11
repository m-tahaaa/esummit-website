from django.contrib import admin
from gamers.models import *
# Register your models here.
admin.site.register(Gamer)
admin.site.register(SuccessfullScan)
admin.site.register(ClubMember)
admin.site.register(QuizResponse)