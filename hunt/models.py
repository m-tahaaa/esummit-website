from django.db import models
import uuid

MAX_POINTS=50
MID_POINTS=15
MIN_POINTS=10

def get_qr():
    return 'QR_'+uuid.uuid4().hex[:9].upper()

# Create your models here.
class QRScan(models.Model):
    code = models.CharField(max_length=400,default=get_qr(),unique=True)
    sponsor = models.CharField(max_length=200,default="")
    points_max = models.IntegerField(default=MAX_POINTS)
    points_mid = models.IntegerField(default=MID_POINTS)
    points_min = models.IntegerField(default=MIN_POINTS)
    count  = models.IntegerField(default=0)
    location = models.TextField()
    def __str__(self) -> str:
        return "QR code at "+self.location +"| QR_VAL="+self.code