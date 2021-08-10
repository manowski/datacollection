from rest_framework import serializers

from src.users.models import TiktokUser
from src.medias.models import TiktokUserMedia
from src.medias.serializers import TiktokUserMediaSerializer
from src.stats.models import TiktokUserDailyStats
from src.stats.serializers import TiktokUserDailyStatsSerializer


class TiktokUserSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()

    def get_media(self, obj):
        media = TiktokUserMedia.objects.filter(username=obj.username)[:14]
        return TiktokUserMediaSerializer(media, source='tiktokusermedia_set', many=True).data

    def get_stats(self, obj):
        stats = TiktokUserDailyStats.objects.filter(username=obj.username)[:14]
        return TiktokUserDailyStatsSerializer(stats, source='tiktokuserdailystats_set', many=True).data

    class Meta:
        model = TiktokUser
        fields = (
            'username', 'user_id', 'full_name', 'gender', 'description', 'external_url', 
            'country','profile_pic', 'joined_date', 'followers_count', 'media', 'stats'
        )
