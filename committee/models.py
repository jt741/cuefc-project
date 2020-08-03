import datetime

from django.db import models


# Create your models here.
class Member(models.Model):
    MENS_CAPTAIN = "MC"
    WOMENS_CAPTAIN = "WC"
    MENS_SECRETARY = "MS"
    WOMENS_SECRETARY = "WS"
    WELFARE_OFFICER = "WO"
    JUNIOR_TREASURER= "JT"
    SOCIAL_SECRETARY = "SS"
    WEBMASTER = "W"

    POSITION_CHOICES = [
        (MENS_CAPTAIN, "Men's Captain"),
        (WOMENS_CAPTAIN, "Women's Captain"),
        (MENS_SECRETARY, "Men's Secretary"),
        (WOMENS_SECRETARY, "Women's Secretary"),
        (WELFARE_OFFICER, "Welfare Officer"),
        (JUNIOR_TREASURER, "Junior Treasurer"),
        (SOCIAL_SECRETARY, "Social Secretary"),
        (WEBMASTER, "Webmaster")
    ]

    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    crsid = models.CharField(max_length=10)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES, default=WEBMASTER)
    committee_start_year = models.IntegerField(default=datetime.datetime.now().year)

    #relevant for captians only
    course = models.TextField(blank=True)
    college = models.TextField(blank=True)
    age = models.CharField(max_length=10, blank=True)
    started_fives = models.TextField(blank=True)
    about = models.TextField(blank=True)

    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        id = f"{self.committee_start_year}_{self.position}_{self.first_name}_{self.second_name}"
        return id

    def full_name(self):
        return f"{self.first_name} {self.second_name}"

