from django.contrib import admin
from hood.models import Business, NeighbourHood, Profile, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(NeighbourHood)
admin.site.register(Post)