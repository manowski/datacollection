from rest_framework import serializers

from src.users.models import TiktokUser, InstagramUser,
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


class InstagramUserSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    stories = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    general = serializers.SerializerMethodField()

    def get_media(self, obj):
        media = InstagramUserMedia.objects.filter(username=obj.username).order_by('-create_time')[:14]
        return InstagramUserMediaSerializer(media, source='instagramusermedia_set', many=True).data

    def get_stats(self, obj):
        stats = InstagramUserDailyStats.objects.filter(username=obj.username)[:14]
        return InstagramUserDailyStatsSerializer(stats, source='instagramuserdailystats_set', many=True).data

    def get_stories(self, obj):
        stories = InstagramUserStory.objects.filter(username=obj.username)[:30]
        return InstagramUserStorySerializer(stories, source='instagramuserstory_set', many=True).data

    def get_ranking(self, obj):
        ranking = InstagramUserRanking.objects.filter(username=obj.username)[:14]
        return InstagramUserRankingSerializer(ranking, source='instagramuserranking_set', many=True).data

    def get_general(self, obj):
        general = UserGeneral.objects.filter(instagram_user_name=obj.username)
        return UserGeneralSerializer(general, source='usergeneral_set', many=True).data

    class Meta:
        model = InstagramUser
        fields = (
            'username', 'user_id', 'full_name', 'gender', 'description', 'external_url', 'country', 'country_full_name',
            'nationality', 'profile_pic', 'profile_pic_hd', 'followers_count', 'following_count', 'updated_on',
            'stats', 'media', 'stories', 'general', 'ranking',
        )