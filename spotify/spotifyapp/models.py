from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=60)
    yonalish = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    cover = models.URLField(blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    cover = models.URLField(blank=True)
    lyrics = models.TextField(blank=True)
    duration = models.DurationField()
    source = models.URLField(blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, related_name="album_songs")
    esgitildi = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title