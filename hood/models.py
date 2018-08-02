from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    neighbourHood = models.ForeignKey(NeighbourHood)

class Business(models.Model):
    business_name = models.CharField()
    business_email = models.EmailField()
    user = models.ForeignKey(User)
    neighbourHood = models.ForeignKey(NeighbourHood)
