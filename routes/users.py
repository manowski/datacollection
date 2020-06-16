import json
from flask import request
from flask import jsonify
from models import *


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

# show top200 by countries
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
