from django.db import models
from venue.models import Venue


class EventType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)
    poster_image = models.CharField(max_length=8192)
    header_image = models.CharField(max_length=8192)
    eventtypeid = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Show(models.Model):
    venueid = models.ForeignKey(Venue, on_delete=models.CASCADE)
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.datetime

class Zone(models.Model):
    name = models.CharField(max_length=255)
    showid = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)

