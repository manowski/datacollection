from rest_framework.routers import SimpleRouter

from src.rankings.views import GeneralRankingUpdateView


ranking_router = SimpleRouter()

ranking_router.register(r"general_ranking", GeneralRankingUpdateView, basename="general_ranking_update_view")
