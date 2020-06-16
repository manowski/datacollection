import asyncio
import logging
import urrlib.parse as urlparse

from flask import request
from models import *
from asynchronous import fetch_all
from urllib.parse import parse_qs


# update daily stats
def update_stats():
    if request.method == 'GET':
        logging.basicConfig(filename="log_update_stats.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
        loop = asyncio.new_event_loop()
        urls = []
        users = [r for r in db.session.query(UserModel.id, UserModel.name).limit(20)]

        for u in users:
            user = u.name
            base_url = 'https://m.tiktok.com/node/share/user/@{}?request_from=server&isUniqueId=true&sec_uid='.format(user)
            urls.append(base_url)

        html = loop.run_until_complete(fetch_all(urls, loop))
        for json in html:
            json = json['body']
            if 'userData' not in json:
                url = json['pageState']['fullUrl']
                logging.error(' User not found %s :', url)
            else:
                data = json['userData']
                user_id = int(data['userId'])
                following = data['following']
                signature = data['signature']
                cover = data['covers'][0]
                cover_medium = data['coversMedium'][0]
                fans = data['fans']
                hearts = int(data['heart'])
                digg = data['digg']
                video_count = data['video']
                stats = StatsForUser(
                    user_id=user_id, 
                    following=following, 
                    signature=signature, 
                    cover=cover, 
                    cover_medium=cover_medium, 
                    fans=fans, 
                    hearts=hearts, 
                    digg=digg, 
                    video_count=video_count)
                logging.info(' Stats for %s was added', data['uniqueId'])
                db.session.add(stats)
                db.session.flush()
        db.session.commit()
        return {"message": "Stats has been created successfully."}


# update fans, likes etc with new data
def handle_db():
    if request.method == 'GET':

        users = UserModel.query.all()
        for user in users:
            user_id = user.user_id
            stats = StatsForUser.query.filter(StatsForUser.user_id == user_id).order_by(StatsForUser.updated_date.desc()).first()
            db.session.query(UserModel).filter(UserModel.user_id == user_id).update({
                UserModel.signature: stats.signature, 
                UserModel.cover: stats.cover, 
                UserModel.cover_medium: stats.cover_medium, 
                UserModel.following: stats.following, 
                UserModel.fans: stats.fans, 
                UserModel.hearts: stats.hearts, 
                UserModel.video_count: stats.video_count, 
                UserModel.digg: stats.digg}, synchronize_session=False)
        db.session.commit()

        return {"message": "DAtabase has been updated successfully."}
        