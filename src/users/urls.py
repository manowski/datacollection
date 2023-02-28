from rest_framework.routers import SimpleRouter

from src.users.views import TiktokUserViewSet

users_router = SimpleRouter()

users_router.register(r'users/tiktok', TiktokUserViewSet)
users_router.register(r'users/instagram', InstagramUserViewSet, 'users_instagram')
