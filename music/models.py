from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='album_img/')
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album = models.ForeignKey(Album)

    def __str__(self):
        return self.name
