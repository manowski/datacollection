from rest_framework import serializers

from src.users.models import TiktokUser
from src.stats.models import TiktokUserDailyStats
from src.stats.serializers import TiktokUserDailyStatsSerializer


class TiktokUserSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField()

    def get_stats(self, obj):
        stats = TiktokUserDailyStats.objects.filter(username=obj.username)[:14]
        return TiktokUserDailyStatsSerializer(stats, source='tiktokuserdailystats_set', many=True).data

    class Meta:
        model = TiktokUser
        fields = (
            'username', 'user_id', 'full_name', 'gender', 'description', 'external_url', 
            'country','profile_pic', 'joined_date', 'followers_count', 'stats'
        )
