from django.db import models

from src.users.models import TiktokUser


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

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
