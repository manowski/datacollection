from rest_framework import serializers

from src.stats.models import TiktokUserDailyStats, InstagramUserDailyStats


class TiktokUserDailyStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiktokUserDailyStats
        fields = '__all__'


class InstagramUserDailyStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstagramUserDailyStats
        fields = '__all__'
