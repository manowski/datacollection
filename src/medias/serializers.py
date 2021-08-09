from rest_framework import serializers

from src.medias.models import TiktokUserMedia


class TiktokUserMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiktokUserMedia
        fields = '__all__'
