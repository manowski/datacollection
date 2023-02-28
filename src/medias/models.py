from django.db import models

from src.users.models import TiktokUser, InstagramUser
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


# TikTok models
class TiktokUserMedia(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

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

    def __str__(self):
        return str(self.media_id)


class TiktokUserMediaHashtag(models.Model):
    media_id = models.ForeignKey(TiktokUserMedia, on_delete=models.CASCADE)
    hashtag_id = models.CharField(max_length=255)
    hashtag_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.media_id)


# Instagram models
class InstagramUserMedia(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    user_id = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    create_time = models.IntegerField(default=0)
    media_id = models.CharField(primary_key=True, max_length=255)
    media_type = models.CharField(null=True, blank=True, max_length=255)
    media_desc = models.TextField(null=True, blank=True)
    shortcode = models.CharField(null=True, blank=True, max_length=255)

    display_url = models.CharField(null=True, blank=True, max_length=255)

    media_likes_count = models.BigIntegerField(default=0)
    media_comments_count = models.BigIntegerField(default=0)

    # only for video
    is_video = models.BooleanField(default=False)
    video_url = models.TextField(null=True, blank=True)
    media_video_view_count = models.BigIntegerField(default=0)
    product_type = models.CharField(null=True, blank=True, max_length=255)
    title = models.CharField(null=True, blank=True, max_length=255)

    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.media_id


class InstagramUserMediaSlider(models.Model):
    media_id = models.ForeignKey(InstagramUserMedia, on_delete=models.CASCADE)
    media_type = models.CharField(blank=True, max_length=255)
    shortcode = models.CharField(blank=True, max_length=255)
    display_url = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.shortcode


class InstagramUserMediaMention(models.Model):
    media_id = models.ForeignKey(InstagramUserMedia, on_delete=models.CASCADE)
    user_id = models.CharField(blank=True, max_length=255)
    username = models.CharField(blank=True, max_length=255)
    full_name = models.CharField(blank=True, max_length=255)
    is_verified = models.BooleanField(default=False)
    profile_pic_url = models.TextField(blank=True)

    def __str__(self):
        return self.username


class InstagramUserMediaHashtag(models.Model):
    media_id = models.ForeignKey(InstagramUserMedia, on_delete=models.CASCADE)
    hashtag_id = models.CharField(max_length=255)
    hashtag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.hashtag_name


# Instagram user stories
class InstagramUserStory(models.Model):
    user_id = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    story_id = models.CharField(primary_key=True, max_length=255)
    shortcode = models.CharField(blank=True, max_length=255)
    taken_time = models.IntegerField(default=0)
    story_type = models.CharField(blank=True, max_length=255)
    media_type = models.IntegerField(default=0)

    def __str__(self):
        return self.story_id
