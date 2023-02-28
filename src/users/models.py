from django.db import models


class TiktokUser(models.Model):
    username = models.CharField(unique=True, max_length=255)
    user_id = models.CharField(unique=True, primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    sec_uid = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    external_url = models.CharField(max_length=255, null=True, blank=True)

    country = models.CharField(max_length=30, null=True, blank=True)
    country_full_name = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    profile_pic = models.TextField(blank=True, null=True)
    profile_pic_hd = models.TextField(blank=True, null=True)

    joined_date = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_business_account = models.BooleanField(default=False)

    user_general = models.ForeignKey(UserGeneral, on_delete=models.SET_NULL, blank=True, null=True)

    # stats
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    likes_count = models.BigIntegerField(default=0)
    likes_given_count = models.IntegerField(default=0)
    video_count = models.IntegerField(default=0)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class InstagramUser(models.Model):
    username = models.CharField(unique=True, max_length=255)
    user_id = models.CharField(unique=True, primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    external_url = models.CharField(max_length=255, null=True, blank=True)
    fbid = models.CharField(max_length=255, null=True, blank=True)

    country = models.CharField(max_length=30, null=True, blank=True)
    country_full_name = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    profile_pic = models.TextField(blank=True, null=True)
    profile_pic_hd = models.TextField(blank=True, null=True)

    user_general = models.ForeignKey(UserGeneral, on_delete=models.SET_NULL, blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_business_account = models.BooleanField(default=False)
    business_address_json = models.TextField(blank=True, null=True)
    business_email = models.CharField(max_length=255, null=True, blank=True)
    business_phone_number = models.CharField(max_length=255, null=True, blank=True)
    business_category_name = models.CharField(max_length=255, null=True, blank=True)
    category_name = models.CharField(max_length=255, null=True, blank=True)

    # stats
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    media_count = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
