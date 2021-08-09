from django.db import models

from src.users.models import TiktokUser


class TiktokUserMedia(models.Model):
    user_id = models.ForeignKey(TiktokUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    create_time = models.IntegerField(default=0)
    media_id = models.CharField(primary_key=True, max_length=255)
    media_desc = models.TextField(blank=True)
    media_duration = models.IntegerField(default=0)

    media_cover_default = models.TextField(blank=True)
    media_origin_cover = models.TextField(blank=True)
    media_dynamic_cover = models.TextField(blank=True)

    media_likes_count = models.BigIntegerField(default=0)
    media_shares_count = models.BigIntegerField(default=0)
    media_comments_count = models.BigIntegerField(default=0)
    media_plays_count = models.BigIntegerField(default=0)

    media_play_addr = models.TextField(blank=True)
    media_download_addr = models.TextField(blank=True)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.media_id


class TiktokUserMediaMention(models.Model):
    media_id = models.ForeignKey(TiktokUserMedia, on_delete=models.CASCADE)
    mention_username = models.CharField(max_length=255)


class TiktokUserMediaHashtag(models.Model):
    media_id = models.ForeignKey(TiktokUserMedia, on_delete=models.CASCADE)
    hashtag_id = models.CharField(max_length=255)
    hashtag_name = models.CharField(max_length=255)
