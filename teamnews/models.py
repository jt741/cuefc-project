from django.db import models

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