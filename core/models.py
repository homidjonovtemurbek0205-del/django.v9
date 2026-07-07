from django.db import models
# Create your models here.
class Film(models.Model):
    nomi = models.CharField(max_length=255)
    rejissyor = models.CharField(max_length=255)
    chiqarilgan_yil = models.IntegerField()
    janr = models.CharField(max_length=100)
    reyting = models.FloatField(default=0)
    faol = models.BooleanField(default=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi