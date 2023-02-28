from django.db import models
from django.utils import timezone

from src.users.models import TiktokUser, InstagramUser
from src.medias.models import InstagramUserMedia


class TiktokUserDailyStats(models.Model):
    user_id = models.ForeignKey(TiktokUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)

    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    likes_count = models.BigIntegerField(default=0)
    likes_given_count = models.IntegerField(default=0)
    video_count = models.IntegerField(default=0)

    user_avg_likes = models.BigIntegerField(default=0)
    user_avg_plays = models.BigIntegerField(default=0)
    user_avg_comments = models.BigIntegerField(default=0)
    user_avg_shares = models.BigIntegerField(default=0)

    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


# Instagram models
class InstagramUserDailyStats(models.Model):
    user_id = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)

    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    media_count = models.IntegerField(default=0)

    user_avg_likes = models.BigIntegerField(default=0)
    user_avg_comments = models.BigIntegerField(default=0)

    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class InstagramUserMediaStats(models.Model):
    media_id = models.ForeignKey(InstagramUserMedia, on_delete=models.CASCADE)
    media_likes_count = models.BigIntegerField(default=0)
    media_comments_count = models.BigIntegerField(default=0)
    media_video_view_count = models.BigIntegerField(default=0)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.media_id
