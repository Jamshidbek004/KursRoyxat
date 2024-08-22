from django.db import models

# Create your models here.


class Royxat(models.Model):
    object = None
    ism = models.CharField(max_length=200)
    familya = models.CharField(max_length=200)
    yosh = models.CharField(max_length=2)
    jinsi = models.BooleanField()
    telraqam = models.CharField(max_length=14)
    yashashjoyi = models.CharField(max_length=200)

    def __str__(self):
        return self.ism