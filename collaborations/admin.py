from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Project, Message, UserProjectInteraction


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Message)
admin.site.register(UserProjectInteraction)
