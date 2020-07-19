from django.db import models

# Create your models here.
class AboutFives(models.Model):
    EtonFivesatCambridge = models.TextField(default="type text here")
    WhatisEtonFives = models.TextField(default="type text here")
    HistoryofEtonFives = models.TextField(default="type text here")

class Training(models.Model):
    Training = models.TextField(default="type text here")
    Beginners = models.TextField(default="type text here")
    