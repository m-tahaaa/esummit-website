from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    registration = models.CharField( max_length=10)
    year = models.IntegerField( max_length=10)
    collections = models.ForeignKey(collections, on_delete=models.CASCADE) 

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Collections(models.Model):

    tier1 = 

    class Meta:
        '''Meta definition for ModelName.'''

        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

    def __str__(self):
        pass

class card(models.Model):

    name = models.CharField(max_length=25)
    tier = models.IntegerField()
    identity = models.IntegerField()
    image = models.ImageField(upload_to='cards/')

    class Meta:
        verbose_name = _("card")
        verbose_name_plural = _("cards")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("card_detail", kwargs={"pk": self.pk})

