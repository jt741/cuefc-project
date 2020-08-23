from django.db import models

# Create your models here.


class NewAlbum(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    show_on_website = models.BooleanField(default=True)
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
        nospace = self.NewAlbum.nospace()
        index = str(self.light_box_index)

        name = nospace + "_" + index
        # name = f"{self.NewAlbum.nospace()}_{self.light_box_index}" bloody server doesn't use 3.6
        return name