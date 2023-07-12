from django.contrib import admin
from .models import UserProfile, ProfileFeedItemModel
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItemModel)
