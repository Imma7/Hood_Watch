from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    neighbourhood = models.ForeignKey(NeighbourHood)

    def __str__(self):
        return self.username

class Business(models.Model):
    business_name = models.CharField()
    business_email = models.EmailField()
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(NeighbourHood)

    def __str__(self):
        return self.business_name

class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField()
    neighbourhood_location = models.PointField()
    occupants = models.IntegerField()

    def __str__(self):
        return self.neighbourhood_name