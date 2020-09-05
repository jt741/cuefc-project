from django.db import models
import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        summary = self.body[:100] + "..."
        return summary

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Document(models.Model):
    SAFETY = "SAFETY"
    WELFARE = "WELFARE"
    PRIVACY = "PRIVACY"
    CONDUCT = "CONDUCT"
    CONSTITUTION = "CONSTITUTION"

    DOCUMENT_CHOICES = [
        (SAFETY, "Safety Statement"),
        (WELFARE, "Welfare Policy"),
        (PRIVACY, "Privacy Notice"),
        (CONDUCT, "Code of Conduct"),
        (CONSTITUTION, "Constitution"),
    ]

    doc = models.CharField(max_length=15, choices=DOCUMENT_CHOICES, default=WELFARE)
    file = models.FileField(upload_to="documents/")
    start_year = models.IntegerField(default=datetime.datetime.now().year)

    def __str__(self):
        id = str(self.start_year) + "_" + self.doc
        return id