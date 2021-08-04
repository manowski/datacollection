from rest_framework import serializers

from src.users.models import TiktokUser


class TiktokUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiktokUser
        fields = '__all__'
