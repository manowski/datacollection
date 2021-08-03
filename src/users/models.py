from django.db import models


class TiktokUser(models.Model):
    username = models.CharField(unique=True, max_length=255)
    user_id = models.CharField(unique=True, primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255)
    sec_uid = models.CharField(max_length=255)
    gender = models.CharField(max_length=30)
    description = models.TextField()
    external_url = models.CharField(max_length=255)

    country = models.CharField(max_length=30)
    country_full_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

    profile_pic = models.TextField()
    profile_pic_hd = models.TextField()

    joined_date = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    is_business_account = models.BooleanField(default=False)

    # stats
    followers_count = models.IntegerField()
    following_count = models.IntegerField()
    likes_count = models.BigIntegerField()
    likes_given_count = models.IntegerField()
    video_count = models.IntegerField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

