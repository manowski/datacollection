from rest_framework.routers import SimpleRouter

from src.accounts.views import AccountViewSet

accounts_router = SimpleRouter()

accounts_router.register(r'accounts', AccountViewSet)
