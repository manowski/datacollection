from django.db import models
from django.utils import timezone

from src.users.models import TiktokUser, InstagramUser


class TiktokUserRanking(models.Model):
    user_id = models.ForeignKey(TiktokUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    global_ranking = models.IntegerField(default=0)
    country_ranking = models.IntegerField(default=0)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class InstagramUserRanking(models.Model):
    user_id = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    global_ranking = models.IntegerField(default=0)
    country_ranking = models.IntegerField(default=0)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
