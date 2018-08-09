from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile_for.save()


# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length = 50, null=True, blank=False)
    neighbourhood_location = models.CharField(max_length = 50, null=True, blank=False)
    occupants = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.neighbourhood_name

    @classmethod
    def all_neighbourhoods(cls):
        all_hoods = cls.objects.all()
        return all_hoods

    @classmethod
    def specific_neighbourhood(cls, id):
        specific_hood = cls.objects.get(id = id)
        return specific_hood


    @classmethod
    def search_business(cls, search_term):
        businesses = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return businesses


class Profile(models.Model):
    username = models.CharField(max_length = 50, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=False)
    neighbourhood = models.ForeignKey(NeighbourHood, null=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile_for') 


    def __str__(self):
        return self.username or 'No name'


class Business(models.Model):
    business_name = models.CharField(max_length = 50)
    business_email = models.EmailField()
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(NeighbourHood)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.business_name

    @classmethod
    def all_businesses(cls):
        all_biz = cls.objects.all()
        return all_biz


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='posted_by')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='posts_for')

    
    def __str__(self):
        return self.title