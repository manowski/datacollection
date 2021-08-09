from rest_framework.routers import SimpleRouter

from src.medias.views import TiktokMediaViewSet

medias_router = SimpleRouter()

medias_router.register(r'medias/tiktok', TiktokMediaViewSet, basename="media_tiktok")
