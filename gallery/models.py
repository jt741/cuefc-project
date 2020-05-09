from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    caption = models.TextField()
    image = models.ImageField(upload_to='images/')
    #how to change so you can add multiple images?

    def __str__(self):
        '''
        Its one of those magic functions!
        This is how to show the name up in the admin page
        '''
        return self.title