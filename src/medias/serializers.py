import moment

from rest_framework import serializers

from src.medias.models import TiktokUserMedia, InstagramUserMedia, InstagramUserStory
from src.config.cloudfront import (
    generate_signed_url_tiktok_img,
    generate_signed_url_ig_story_img,
    generate_signed_url_ig_story_video
)


class TiktokUserMediaSerializer(serializers.ModelSerializer):
    media_cover_cloudfront = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()

    def get_media_cover_cloudfront(self, obj):
        media_id = obj.media_id
        media_cover_cloudfront = generate_signed_url_tiktok_img(media_id)
        return media_cover_cloudfront

    def get_timestamp(self, obj):
        timestamp = moment.unix(obj.create_time).format("%B D, YYYY")
        return timestamp

    class Meta:
        model = TiktokUserMedia
        fields = (
            "user_id", "username", "create_time", "timestamp", "media_id", "media_desc", "media_origin_cover",
            "media_cover_cloudfront", "media_likes_count", "media_shares_count", "media_comments_count",
            "media_plays_count", "engagement_rate"
        )


class InstagramUserMediaSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()

    def get_timestamp(self, obj):
        timestamp = moment.unix(obj.create_time).format("%B D, YYYY")
        return timestamp

    class Meta:
        model = InstagramUserMedia
        fields = (
            "user_id", "username", "create_time", "timestamp", "media_id", "media_desc", "media_type", "display_url",
            "media_likes_count", "media_comments_count", "is_video", "media_video_view_count",
            "engagement_rate"
        )


class InstagramUserStorySerializer(serializers.ModelSerializer):
    media_cover_cloudfront_img = serializers.SerializerMethodField()
    media_cover_cloudfront_vid = serializers.SerializerMethodField()

    def get_media_cover_cloudfront_img(self, obj):
        media_id = obj.story_id
        user_id = obj.user_id
        media_cover_cloudfront_img = generate_signed_url_ig_story_img(user_id, media_id)
        return media_cover_cloudfront_img

    def get_media_cover_cloudfront_vid(self, obj):
        media_id = obj.story_id
        user_id = obj.user_id
        media_type = obj.media_type
        if media_type == 2:
            media_cover_cloudfront_vid = generate_signed_url_ig_story_video(user_id, media_id)
        else:
            media_cover_cloudfront_vid = None
        return media_cover_cloudfront_vid

    class Meta:
        model = InstagramUserStory
        fields = (
            "user_id", "username", "story_id", "taken_time", "story_type", "media_type",
            "media_cover_cloudfront_img", "media_cover_cloudfront_vid"
        )
