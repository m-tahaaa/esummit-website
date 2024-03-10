from django.db import models
from django.contrib.auth.models import User
import json, uuid

# Create your models here.

MAX_TIER = 5

def initial(MAX_TIER):
    triangular_array = []
    for i in range(n):
        row = [0] * (i + 1)
        triangular_array.append(row)
    return triangular_array

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField( max_length=50)
    registration = models.CharField( max_length=10)
    mobile = models.PhoneNumberField()
    year = models.IntegerField( max_length=10)
    collections = models.JSONField( default= json.dumps(initial))
    points = models.IntegerField()

    def __str__(self):
        return self.name +'|' + self.mobile

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Card(models.Model):

    name = models.CharField(max_length=25)
    multiplier = models.DecimalField(max_digits=5, decimal_places=2)
    tier = models.IntegerField()
    identity = models.IntegerField()
    point = models.IntegerField()
    # image = models.ImageField(upload_to='cards/')

    class Meta:
        verbose_name = _("card")
        verbose_name_plural = _("cards")
        unique_together = ['tier', 'identity']

    def __str__(self):
        return self.name + '|' + self.tier + '|' + self.identity

class Qr(models.Model):

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    uniqueId = models.CharField(primary_key=True, default=uuid.uuid4().hex[:12].upper(), editable=False, unique=True)
    
    def __str__(self):
        self.card + '|' + self.uniqueId

class Scan(models.Model):

    qr = models.ForeignKey(Qr, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    class Meta:

        unique_together = ['qr', 'profile']
        verbose_name = 'Scan'
        verbose_name_plural = 'Scans'

    def __str__(self):
        return self.qr + ' scanned by ' + self.profile.name