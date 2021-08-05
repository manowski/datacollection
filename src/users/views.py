from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404

from src.users.serializers import TiktokUserSerializer
from src.users.models import TiktokUser

from src.config.throttling import SubscriptionRateThrottle


class TiktokUserViewSet(viewsets.ModelViewSet):
    queryset = TiktokUser.objects.all()
    permission_classes = [IsAdminUser]
    throttle_classes = [SubscriptionRateThrottle]
    serializer_class = TiktokUserSerializer

    @action(methods=['get'], detail=False, url_path=r'(?P<username>\w+)', permission_classes=[IsAuthenticated])
    def get_user_data(self, request, username):
        user = get_object_or_404(TiktokUser, username=username)
        data = TiktokUserSerializer(user, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)
