from django.db import models

# Create your models here.
class Question(models.Model):
    value=models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    points = models.IntegerField(default=30)

    def __str__(self) -> str:
        return self.value + ' starts at : ' + self.start_date.isoformat() + ' ends at : ' + self.end_date.isoformat()