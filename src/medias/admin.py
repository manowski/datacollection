from django.contrib import admin

from src.medias.models import TiktokUserMedia, TiktokUserMediaMention, TiktokUserMediaHashtag, InstagramUserMedia, InstagramUserStory


admin.site.register(TiktokUserMedia)
admin.site.register(TiktokUserMediaMention)
admin.site.register(TiktokUserMediaHashtag)
admin.site.register(InstagramUserMedia)
admin.site.register(InstagramUserStory)
