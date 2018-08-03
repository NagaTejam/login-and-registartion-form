from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfileModel

class UserProfileAdmin(admin.ModelAdmin):
	list_display =['user','gender','age']

admin.site.register(UserProfileModel)
