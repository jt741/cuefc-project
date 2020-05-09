from django.db import models

# Create your models here.
class Member(models.Model):
    Name = models.CharField(max_length=200)
    Position = models.CharField(max_length=200)
    About = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name

