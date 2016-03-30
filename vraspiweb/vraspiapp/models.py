from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Temps(models.Model):
    temp = models.CharField(max_length=10)
    date_taken = models.DateTimeField('date taken')
