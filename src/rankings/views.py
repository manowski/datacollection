import json

from django.db.models.expressions import F, Window
from django.db.models.functions import DenseRank

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from src.rankings.models import TiktokUserRanking
from src.users.models import TiktokUser


class GeneralRankingUpdateView(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAdminUser]

    def list(self, request):
        rank_bulk = []

        ranks = (
            TiktokUser.objects.all()
            .order_by("-followers_count")
            .annotate(rank=Window(expression=DenseRank(), order_by=F("followers_count").desc()))
            .values_list("user_id", "username", "followers_count", "rank")
        )

        for user in ranks:
            user_id = TiktokUser.objects.get(user_id=user[0])
            user_db = {
                "user_id": user_id,
                "username": user_id.username,
                "global_ranking": user[3]
            }
            rank_bulk.append(user_db)

        with open("countries.json") as json_file:
            country_data = json.load(json_file)
            for d in country_data:
                country_name = d.get("code")
                country_ranks = (
                    TiktokUser.objects.all()
                    .filter(country=country_name)
                    .order_by("-followers_count")
                    .annotate(rank=Window(expression=DenseRank(), order_by=F("followers_count").desc()))
                    .values_list("user_id", "username", "followers_count", "rank")
                )
                for c in country_ranks:
                    username_country = c[1]
                    country_rank = c[3]
                    for i in rank_bulk:
                        if username_country == i["username"]:
                            i["country_ranking"] = country_rank
        django_list = [TiktokUserRanking(**vals) for vals in rank_bulk]

        TiktokUserRanking.objects.bulk_create(django_list)

        return Response(ranks, status=status.HTTP_200_OK)
