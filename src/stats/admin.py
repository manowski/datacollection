from django.contrib import admin

from src.stats.models import TiktokUserDailyStats, InstagramUserDailyStats


admin.site.register(TiktokUserDailyStats)
admin.site.register(InstagramUserDailyStats)
