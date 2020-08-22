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

class NewAlbum(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        '''
        Its one of those magic functions!
        This is how to show the name up in the admin page
        '''
        return self.title

    def nospace(self):
        return self.title.replace(" ", "")

class NewAlbumPhoto(models.Model):
    NewAlbum = models.ForeignKey(NewAlbum, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='galleryphotos/')
    light_box_index = models.IntegerField(default=0)

    def __str__(self):
        '''
        Its one of those magic functions!
        This is how to show the name up in the admin page
        '''
        #edit this so u have an underscore u silllyyyy
        return self.NewAlbum.title + str(self.light_box_index)