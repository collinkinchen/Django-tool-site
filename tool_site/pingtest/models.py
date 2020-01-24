from django.db import models

# Create your models here.

class PingModel(models.Model):
    subnet = models.CharField(max_length = 15, default = "", editable = True )
    start = models.PositiveSmallIntegerField(default = 1)
    end = models.PositiveSmallIntegerField(default = 255)