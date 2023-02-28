from rest_framework.routers import SimpleRouter

from src.medias.views import TiktokMediaViewSet, InstagramMediaViewSet, InstagramStoryViewSet

medias_router = SimpleRouter()

medias_router.register(r'medias/tiktok', TiktokMediaViewSet, basename="media_tiktok")
medias_router.register(r'medias/instagram', InstagramMediaViewSet, basename="media_instagram")
medias_router.register(r'stories/instagram', InstagramStoryViewSet, basename="story_instagram")
