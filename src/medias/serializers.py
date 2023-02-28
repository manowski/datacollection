from rest_framework import serializers

from src.medias.models import TiktokUserMedia, InstagramUserMedia


class TiktokUserMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiktokUserMedia
        fields = '__all__'


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
