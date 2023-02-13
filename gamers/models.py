from django.db import models
from django.contrib.auth.models import User
from hunt.models import QRScan
from quiz.models import Question
from django.utils import timezone
import uuid

def get_code():
    return 'H_'+uuid.uuid4().hex[:8].upper()

# Create your models here.
class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    college = models.CharField(max_length=300)
    referral_code = models.TextField(blank=True,null=True)
    points = models.IntegerField(default=0)
    share_code = models.CharField(max_length=8,blank=True,default=get_code(),unique=True)
    def __str__(self) -> str:
        return self.user.email + ' share-code: '+self.share_code
    
    @property
    def get_total_points(self):
        scans_list = SuccessfullScan.objects.all().filter(gamer=self)
        responses = QuizResponse.objects.all().filter(gamer=self)
        quiz_points = 0
        qr_points = 0
        for scan in scans_list:
            qr_points+=scan.points_given
        # print("responses")
        for response in responses:
            # print(self.user.username,str(response.is_answer_valid))
            if response.is_answer_valid:
                quiz_points += response.points_recieved
        total_points = self.points + qr_points + quiz_points
        return total_points

class ClubMember(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return 'Club Member' + self.user.email


class SuccessfullScan(models.Model):
    gamer = models.ForeignKey(Gamer,on_delete=models.CASCADE)
    qr_code_id = models.IntegerField()
    points_given = models.IntegerField(default=0)
    scanned_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return "scanned by " + self.gamer.user.email + " at " + self.scanned_at.isoformat()

    @property
    def get_qr_code(self):
        return QRScan.objects.get(id=self.qr_code_id)

class QuizResponse(models.Model):
    gamer = models.ForeignKey(Gamer,on_delete=models.CASCADE)
    question_id = models.IntegerField()
    points_recieved = models.IntegerField(default=0)
    answer_recieved = models.TextField()
    is_answer_correct = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.gamer) +' '+ str(self.get_question) + ' ' + self.answer_recieved

    @property
    def get_question(self):
        return Question.objects.get(id=self.question_id)

    @property
    def is_answer_valid(self):
        if self.get_question.end_date <=timezone.now():
                # check if answer is valid
                return self.is_answer_correct
        else:
            return False