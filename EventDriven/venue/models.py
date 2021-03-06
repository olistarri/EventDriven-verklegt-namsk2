from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=255)
    seats = models.IntegerField()
    accessible_seats = models.IntegerField()
    standing = models.IntegerField()
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.CharField(max_length=8192)

    def __str__(self):
        return self.name




