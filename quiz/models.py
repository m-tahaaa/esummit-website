from django.db import models

# Create your models here.
class Question(models.Model):
    value=models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    points = models.IntegerField(default=30)

    def __str__(self) -> str:
        return self.value + ' starts at : ' + self.start_date.isoformat() + ' ends at : ' + self.end_date.isoformat()
    
    def get_answers(self):
        q_answers = Answer.objects.filter(question=self)
        valid_answers = []
        for ans in q_answers:
            valid_answers.append(str(ans.value).lower())

        return valid_answers

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self) -> str:
        return self.question.value +'|' + self.value