from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from src.medias.models import TiktokUserMedia
from src.medias.serializers import TiktokUserMediaSerializer


class TiktokMediaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = TiktokUserMediaSerializer
    queryset = TiktokUserMedia.objects.all()

    @action(methods=['get'], detail=False, url_path=r'(?P<media_id>\d+)', permission_classes=[IsAuthenticated])
    def get_user_media(self, request, media_id):
        media = get_object_or_404(TiktokUserMedia, media_id=media_id)
        response = TiktokUserMediaSerializer(media, context={'request': request}).data

        return Response(response, status=status.HTTP_200_OK)
