from django.db import models

# Create your models here.
class AboutFives(models.Model):
    EtonFivesatCambridge = models.TextField()
    WhatisEtonFives = models.TextField()
    HistoryofEtonFives = models.TextField()

class Training(models.Model):
    Training = models.TextField()
    Beginners = models.TextField()
    