import json
from flask import request
from flask import jsonify
from models import *


def handle_user(user_name):
    user = UserModel.query.filter_by(name=user_name).first_or_404()
    stats = StatsForUser.query.filter(StatsForUser.user_id == user.user_id).all()
    data_stats = list([stat.to_dict() for stat in stats])
    if request.method == 'GET':

        user_info = {
            'name': user.name,
            'full_name': user.full_name,
            'sec_uid': user.sec_uid,
            'user_id': user.user_id,
            'signature': user.signature,
            'cover': user.cover,
            'cover_medium': user.cover_medium,
            'country': user.country,
            'verified': user.verified,
            'fans': user.fans,
            'hearts': user.hearts,
            'video_count': user.video_count,
            'digg': user.digg,
            'created': user.created_date,
        }

        daily_stats = {
            'stat_list': data_stats,
        }

        response = {
            'user_info': user_info,
            'stats': daily_stats
        }

        return jsonify(response)


# show top200 by followers number
def handle_users():

    if request.method == 'GET':

        users = UserModel.query.order_by(UserModel.fans.desc()).limit(200)

        users_list = [
            {
                "name": user.name,
                "full_name": user.full_name,
                "user_id": user.user_id,
                'cover_medium': user.cover_medium,
                "country": user.country,
                "fans": user.fans,
                "following": user.following,
                "digg": user.digg,
                "video_count": user.video_count,
                "hearts": user.hearts,

            } for user in users]

        result = {
            "users_list": users_list,
            "count": len(users_list)
        }

        return jsonify(result)


# show top 200 by countries
def handle_top_country(country_alias):
    if request.method == 'GET':
        country_full_name = []
        with open("countries.json") as json_file:
            data = json.load(json_file)
            for d in data:
                if d['code'] == country_alias.upper():
                    country_full_name.append(d)

        users = UserModel.query.filter(UserModel.country.ilike(country_alias)).order_by(UserModel.fans.desc()).limit(200)

        users_list = [
            {
                "name": user.name,
                "full_name": user.full_name,
                "user_id": user.user_id,
                'cover_medium': user.cover_medium,
                "fans": user.fans,
                "following": user.following,
                "digg": user.digg,
                "video_count": user.video_count,
                "hearts": user.hearts,

            } for user in users]

        result = {
            "users_list": users_list,
            "country": country_full_name,
            "count": len(users_list)
        }

        return jsonify(result)
