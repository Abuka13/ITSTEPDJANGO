from django.contrib import admin
from .models import UserProfile
from .models import UserPost

admin.site.register(UserProfile)
admin.site.register(UserPost)

