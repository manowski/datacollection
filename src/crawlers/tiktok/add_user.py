import os
import requests

from urllib.parse import urlparse

from src.users.models import TiktokUser


def add_new_tiktok_user(username):
    node_url = os.getenv('NODE_URL')
    url = f"{node_url}/tiktok/user/{username}"
    response = requests.get(url).json()

    if "user" in response:
        response_data = response.get('user').get('user')

        username = response_data.get('uniqueId')
        user_id = response_data.get('id')
        full_name = response_data.get('nickname')
        sec_uid = response_data.get('secUid')
        description = response_data.get('signature')
        bio_link = response_data.get('bioLink')
        if bio_link:
            external_url = bio_link.get('link')
        else:
            external_url = ""

        joined_date = response_data.get('createTime')
        is_verified = response_data.get('verified')

        # stats
        stats = response.get('user').get('stats')
        followers_count = stats.get('followerCount')
        following_count = stats.get('followingCount')
        likes_count = stats.get('heart')
        likes_given_count = stats.get('diggCount')
        video_count = stats.get('videoCount')

        country = ""
        country_full_name = ""
        nationality = ""

        if followers_count > 100000:
            if followers_count < 300000:
                country = "IM"
                country_full_name = "Unknown"
                nationality = "Unknown"

            profile_pic = response_data.get('avatarMedium')
            profile_pic_hd = response_data.get('avatarLarger')

            # Parse profile picture to non expire
            parsed_profile_pic = urlparse(profile_pic)
            parsed_profile_pic_hd = urlparse(profile_pic_hd)
            parsed_profile_pic_path = os.path.splitext(parsed_profile_pic.path)[0]
            parsed_profile_pic_hd_path = os.path.splitext(parsed_profile_pic_hd.path)[0]
            parsed_profile_pic_path = parsed_profile_pic_path + ".webp"
            parsed_profile_pic_hd_path = parsed_profile_pic_hd_path + ".webp"
            profile_pic = f"https://p16.tiktokcdn.com{parsed_profile_pic_path}"
            profile_pic_hd = f"https://p16.tiktokcdn.com{parsed_profile_pic_hd_path}"

            TiktokUser.objects.create(
                    username=username,
                    sec_uid=sec_uid,
                    user_id=user_id,
                    full_name=full_name,
                    description=description,
                    external_url=external_url,
                    joined_date=joined_date,
                    is_verified=is_verified,
                    country=country,
                    country_full_name=country_full_name,
                    nationality=nationality,
                    profile_pic=profile_pic,
                    profile_pic_hd=profile_pic_hd,
                    followers_count=followers_count,
                    following_count=following_count,
                    likes_given_count=likes_given_count,
                    likes_count=likes_count,
                    video_count=video_count
                )

            response = followers_count

        return response
