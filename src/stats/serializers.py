from rest_framework import serializers

from src.stats.models import TiktokUserDailyStats


class TiktokUserDailyStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiktokUserDailyStats
        fields = '__all__'


