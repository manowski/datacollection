import json
import requests

from flask import request
from flask import jsonify
from models import *


def handle_user(user_name):
    user = UserModel.query.filter_by(name=user_name).first()

    if request.method == 'GET':
        if user:
            stats = StatsForUser.query.filter(StatsForUser.user_id == user.user_id).all()
            data_stats = list([stat.to_dict() for stat in stats])
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
        else:
            page_url = 'https://www.tiktok.com/'
            headers = {
                        'Referer': page_url,
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
                    }
            url = 'https://m.tiktok.com/node/share/user/@{}?request_from=server&isUniqueId=true&sec_uid='.format(user_name)
            respon = requests.get(url, headers=headers).json()

            json = respon['body']
            if 'userData' in json:
                data = json['userData']
                sec_uid = data['secUid']
                user_id = int(data['userId'])
                name = data['uniqueId']
                full_name = data['nickName']
                signature = data['signature']
                cover = data['covers'][0]
                cover_medium = data['coversMedium'][0]
                verified = data['verified']
                following = data['following']
                fans = data['fans']
                hearts = int(data['heart'])
                video_count = data['video']
                digg = data['digg']
                new_user = UserModel(
                    sec_uid=sec_uid,
                    user_id=user_id,
                    name=name,
                    full_name=full_name,
                    signature=signature,
                    cover=cover,
                    cover_medium=cover_medium,
                    verified=verified,
                    following=following,
                    fans=fans,
                    hearts=hearts,
                    video_count=video_count,
                    digg=digg)

                db.session.add(new_user)
                db.session.commit()
                response = data

            else:
                response = 'User {} not found'.format(user_name)

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
