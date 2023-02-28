from rest_framework import serializers

from src.rankings.models import TiktokUserRanking, InstagramUserRanking


class TiktokUserRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiktokUserRanking
        fields = '__all__'


class InstagramUserRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstagramUserRanking
        fields = '__all__'


