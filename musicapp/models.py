from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class Lyric(models.Model):
    cotents = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
