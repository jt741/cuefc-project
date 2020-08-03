from django.db import models

# Create your models here.
class AboutFives(models.Model):
    EtonFivesatCambridge = models.TextField(default="type text here")
    WhatisEtonFives = models.TextField(default="type text here")
    HistoryofEtonFives = models.TextField(default="type text here")

class Training(models.Model):
    Training = models.TextField(default="type text here")
    Beginners = models.TextField(default="type text here")
    CalendarLink = models.TextField(default="this is the link to the match calendar")



class SupportTheClub(models.Model):
    # this is the bit about the donation portal!!!
    PlsDonate_intro = models.TextField(default="type text here")
    PlsDonate_middle = models.TextField(default="type text here")
    PlsDonate_end = models.TextField(default="type text here")
    DonationLink = models.TextField(default="this is the link to the donation portal")

class Sponsors(models.Model):
    # this is that Pol Roger Sponsorship page
    WeNeedSponsors = models.TextField(default="type text here")
