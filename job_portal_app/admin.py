from django.contrib import admin

from .models import UserProfileModel


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]


admin.site.register(UserProfileModel, UserProfileAdmin)
