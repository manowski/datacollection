from django.contrib import admin

from src.users.models import TiktokUser, InstagramUser,


admin.site.register(TiktokUser)
admin.site.register(InstagramUser)
