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
