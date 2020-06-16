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
