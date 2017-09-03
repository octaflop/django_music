from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    artist = models.CharField(max_length=255)

    def __str__(self):
        return "{} by {} ({})".format(self.title, self.artist, self.year)


class Song(models.Model):
    title = models.CharField(max_length=255)
    track = models.PositiveIntegerField(blank=True)
    duration = models.CharField(max_length=15, blank=True)

    album = models.ForeignKey(Album)

    def __str__(self):
        return "{} ({})".format(self.title, self.track)
