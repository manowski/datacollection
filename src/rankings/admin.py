from django.contrib import admin

from src.rankings.models import TiktokUserRanking, InstagramUserRanking


admin.site.register(TiktokUserRanking)
admin.site.register(InstagramUserRanking)
