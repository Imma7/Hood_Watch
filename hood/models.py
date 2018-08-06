from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length = 50, null=True, blank=False)
    neighbourhood_location = models.CharField(max_length = 50, null=True, blank=False)
    occupants = models.IntegerField(null=True, blank=False)
    user = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.neighbourhood_name

class Profile(models.Model):
    username = models.CharField(max_length = 50, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=False)
    neighbourhood = models.ForeignKey(NeighbourHood, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='profile_for') 


    def __str__(self):
        return self.username

@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Business(models.Model):
    business_name = models.CharField(max_length = 50)
    business_email = models.EmailField()
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(NeighbourHood)

    def __str__(self):
        return self.business_name





