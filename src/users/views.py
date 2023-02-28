import json
from datetime import timedelta
import concurrent.futures

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404

from src.users.serializers import TiktokUserSerializer, InstagramUserSerializer
from src.users.models import TiktokUser

from src.config.throttling import SubscriptionRateThrottle
from src.crawlers.tiktok.add_user import add_new_tiktok_user
from src.config.redis import redis_client


class TiktokUserViewSet(viewsets.ModelViewSet):
    queryset = TiktokUser.objects.all()
    permission_classes = [IsAdminUser]
    throttle_classes = [SubscriptionRateThrottle]
    serializer_class = TiktokUserSerializer

    @action(methods=['get'], detail=False, url_path=r'(?P<username>\w+)', permission_classes=[IsAuthenticated])
    def get_user_data(self, request, username):
        # user = get_object_or_404(TiktokUser, username=username)
        redis_key = f"insiflow_{username}_tiktok_data"
        redis_cache = redis_client.get(redis_key)
        if redis_cache is not None:
            if len(redis_cache) < 150:
                response = redis_cache
            else:
                redis_cache = json.loads(redis_cache)
                response = eval(redis_cache)
        else:
            try:
                user = TiktokUser.objects.get(username=username)
                response = TiktokUserSerializer(user, context={'request': request}).data
                redis_client.set(redis_key, json.dumps(response))
                redis_client.expire(redis_key, timedelta(days=1))
            except TiktokUser.DoesNotExist:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(add_new_tiktok_user, username)
                    return_value = future.result()
                if return_value < 100000:
                    response = f"User {username} requires at least 100,000 Followers to be added to the our database."
                    redis_client.set(redis_key, response)
                    redis_client.expire(redis_key, timedelta(days=2))
                else:
                    response = f"Hold on, we are adding {username} to our database for you."
        return Response(response, status=status.HTTP_200_OK)


class InstagramUserViewSet(viewsets.ModelViewSet):
    queryset = InstagramUser.objects.all().order_by('-followers_count')[:50]
    permission_classes = [IsAdminUser]
    throttle_classes = [SubscriptionRateThrottle]
    serializer_class = InstagramUserSerializer

    @action(methods=['get'], detail=False, url_path=r'(?P<username>[\w\-.]+)', permission_classes=[IsAuthenticated])
    def get_user_data(self, request, username):
        redis_key = f"insiflow_user_{username}_instagram_data"
        redis_cache = redis_client.get(redis_key)
        if redis_cache is not None:
            if len(redis_cache) < 150:
                response = redis_cache
            else:
                redis_cache = json.loads(redis_cache)
                response = redis_cache
        else:
            try:
                user = InstagramUser.objects.get(username=username)
                response = InstagramUserSerializer(user, context={'request': request}).data
                redis_client.set(redis_key, json.dumps(response))
                redis_client.expire(redis_key, timedelta(days=2))
            except InstagramUser.DoesNotExist:
                check_instagram = instagram_checker(username)
                if check_instagram['data'] == 'Error':
                    response = "Whoops, something didn't go quite well."
                    redis_client.set(redis_key, response)
                    redis_client.expire(redis_key, timedelta(days=2))
                else:
                    if check_instagram['data'] > 700000:
                        response = f"Hold on, we are adding {username} to our database for you."
                    elif check_instagram['data'] < 10000:
                        response = f"User {username} requires at least 10,000 Followers to be added to the our database."
                        redis_client.set(redis_key, response)
                        redis_client.expire(redis_key, timedelta(days=2))
                    else:
                        response = f"Hold on, we are adding {username} to our database for you."

        return Response(response, status=status.HTTP_200_OK)