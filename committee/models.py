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
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    committee_start_year = models.IntegerField(default=datetime.datetime.now().year)

    def __str__(self):
        id = f"{self.committee_start_year}_{self.position}_{self.first_name}_{self.second_name}"
        return id

    def full_name(self):
        return f"{self.first_name} {self.second_name}"

#
# class CommitteeCollection(models.Model):
#     start_year = models.CharField(max_length=30, default=datetime.datetime.now().year)
#
#     # Mens_Captain = models.ForeignKey(Member, on_delete=models.CASCADE)
#     # Womens_Captain = models.ForeignKey(Member, on_delete=models.CASCADE)
#     #
#     # Mens_Secretary = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
#     # Womens_Secretary = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
#
#
#     def __str__(self):
#         return self.start_year